import unittest
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
        new_dir = "this is the new text"
        original_dir = ServerCompilerSettings().compiler_dir
        self.assertEqual(original_dir, ServerCompilerSettings()._compiler_dir)
        
        ServerCompilerSettings().compiler_dir = new_dir
        self.assertEqual(new_dir, ServerCompilerSettings().compiler_dir)
        self.assertNotEqual(original_dir, ServerCompilerSettings().compiler_dir)
    
    #
    # Testing the settings file
    #
    def test_settings_file_creation(self):
        ServerCompilerSettings().save_settings()


if __name__ == '__main__':
    unittest.main()
