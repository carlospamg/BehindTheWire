from __future__ import unicode_literals
import os
import unittest
import mock
import ParentDirToSysPath
from ServerCompilerSettings import ServerCompilerSettings


class ServerCompilerSettingsTestCase(unittest.TestCase):
    """
    Tests for ServerCompilerSettings
    """
    
    #
    # Testing the class singlentoness
    #
    def test_singleton(self):
        # Testing if singleton is working
        instance_1 = ServerCompilerSettings()
        instance_2 = ServerCompilerSettings()
        self.assertEqual(id(instance_1), id(instance_2))
    
    #
    # Testing the compiler_dir getter and setter
    #
    def test_read_compiler_dir(self):
        self.assertEqual(ServerCompilerSettings().compiler_dir, ServerCompilerSettings().__compiler_dir__)

    @mock.patch('ServerCompilerSettings.os')
    def test_write_compiler_dir_invalid(self, mock_os):
        """
        Tests path doesn't get save if:
             A file that does not exists
             Just a folder
             A non executable file
        """
        # TODO: a file that exists and does not execute is not done
        # Random file
        mock_os.path.exists.return_value = False
        original_dir = ServerCompilerSettings().compiler_dir
        new_dir = os.path.join(os.getcwd(), 'random.exe')
        ServerCompilerSettings().compiler_dir = new_dir
        self.assertNotEqual(new_dir, ServerCompilerSettings().compiler_dir)
        self.assertEqual(original_dir, ServerCompilerSettings().compiler_dir)

        # Just a folder
        mock_os.path.exists.return_value = True
        new_dir = os.getcwd()
        ServerCompilerSettings().compiler_dir = new_dir
        self.assertNotEqual(new_dir, ServerCompilerSettings().compiler_dir)
        self.assertEqual(original_dir, ServerCompilerSettings().compiler_dir)

        # Non .exe file
        mock_os.path.exists.return_value = True
        new_dir = os.path.join(os.getcwd(), 'arduino.txt')
        ServerCompilerSettings().compiler_dir = new_dir
        self.assertNotEqual(new_dir, ServerCompilerSettings().compiler_dir)
        self.assertEqual(original_dir, ServerCompilerSettings().compiler_dir)

    @mock.patch('ServerCompilerSettings.os')
    def test_write_compiler_dir_valid(self, mock_os):
        mock_os.path.exists.return_value = True
        new_dir = os.path.join(os.getcwd(), 'arduino.exe')
        ServerCompilerSettings().compiler_dir = new_dir
        self.assertEqual(new_dir, ServerCompilerSettings().compiler_dir)

    #
    # Testing the settings file
    #
    def test_settings_file_creation(self):
        """ Need to find a way to test this one """
        ServerCompilerSettings().save_settings()
        self.assertEqual(0,0)


if __name__ == '__main__':
    unittest.main()
