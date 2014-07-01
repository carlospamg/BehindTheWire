import unittest
import mock
import ParentDirToSysPath
import BlocklyRequestHandler


class BlocklyRequestHandlerTestCase(unittest.TestCase):
    """
    Tests for BlocklyRequestHandler module
    """
    
    def test_command_line(self):
        """
        Tests that a compiler path and arduino sketch path cam ne set
        and that a command line can be launched to open the sketch in the
        Arduino IDE
        """
        BlocklyRequestHandler.set_compiler_path()
        BlocklyRequestHandler.execute_command_line()

    #@mock.patch('BlocklyRequestHandler.os')
    #def test_compiler_path(self, mock_os):
    #    new_comp_path = BlocklyRequestHandler.set_compiler_path()
    #    #mock_os.remove.assert_called_with()
    #    self.assertEqual(new_comp_path, BlocklyRequestHandler.get_compiler_path())

if __name__ == '__main__':
    unittest.main()
