import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from services.process_service import get_system_stats

class TestProcessService(unittest.TestCase):

    @patch('services.process_service.psutil')
    @patch('services.process_service.time.sleep')
    def test_get_system_stats(self, mock_sleep, mock_psutil):
        # Mock CPU
        mock_psutil.cpu_percent.return_value = 45.5

        # Mock RAM
        mock_ram = MagicMock()
        mock_ram.percent = 60.2
        mock_ram.used = 8 * (1024 ** 3)
        mock_ram.total = 16 * (1024 ** 3)
        mock_psutil.virtual_memory.return_value = mock_ram

        # Mock Disk
        mock_disk = MagicMock()
        mock_disk.free = 500 * (1024 ** 3)
        mock_disk.total = 1000 * (1024 ** 3)
        mock_psutil.disk_usage.return_value = mock_disk

        # Mock Temperature
        mock_temp_entry = MagicMock()
        mock_temp_entry.current = 65.5
        mock_psutil.sensors_temperatures.return_value = {
            'coretemp': [mock_temp_entry]
        }

        # Mock Network
        mock_net1 = MagicMock()
        mock_net1.bytes_recv = 1000
        mock_net1.bytes_sent = 500
        mock_net2 = MagicMock()
        mock_net2.bytes_recv = 3000
        mock_net2.bytes_sent = 1500
        mock_psutil.net_io_counters.side_effect = [mock_net1, mock_net2]

        result = get_system_stats()

        # Assertions
        self.assertEqual(result["cpu"], "45.5%")
        self.assertEqual(result["ram"], "60.2%,8.0/16.0 GB")
        self.assertEqual(result["disk"], "500.0/1000.0")
        self.assertEqual(result["cpu_temp"], "65.5°C")
        self.assertEqual(result["net"], "↓ 2.0 KB/s ↑ 1.0 KB/s")

if __name__ == '__main__':
    unittest.main()