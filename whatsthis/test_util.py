# This file is part of whatsthis. See LICENSE file for license information.
"""Test util.py."""
import subprocess
from unittest import mock

from whatsthis.util import execute


@mock.patch.object(subprocess, 'Popen')
def test_execute(m_popen):
    """Return True when systemd-detect virt exits success."""
    mock_communicate_method = mock.MagicMock()
    mock_communicate_method.return_value = (b'my_file', b'')

    process_mock = mock.MagicMock()
    process_mock.communicate = mock_communicate_method
    process_mock.returncode = 0
    m_popen.return_value = process_mock

    out, err, returncode = execute(['ls'])

    assert out == 'my_file'
    assert err == ''
    assert returncode == 0


@mock.patch.object(subprocess, 'Popen')
def test_execute_string(m_popen):
    """Return True when systemd-detect virt exits success."""
    mock_communicate_method = mock.MagicMock()
    mock_communicate_method.return_value = (b'my_file', b'')

    process_mock = mock.MagicMock()
    process_mock.communicate = mock_communicate_method
    process_mock.returncode = 0
    m_popen.return_value = process_mock

    out, err, returncode = execute('ls')

    assert out == 'my_file'
    assert err == ''
    assert returncode == 0


@mock.patch.object(subprocess, 'Popen')
def test_execute_badcmd(m_popen):
    """Return True when systemd-detect virt exits success."""
    mock_communicate_method = mock.MagicMock()
    mock_communicate_method.return_value = (b'', b'Command not found')

    process_mock = mock.MagicMock()
    process_mock.communicate = mock_communicate_method
    process_mock.returncode = 1
    m_popen.return_value = process_mock

    out, err, returncode = execute('fake_cmd')

    assert out == ''
    assert err == 'Command not found'
    assert returncode == 1
