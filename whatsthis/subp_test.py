# This file is part of whatsthis. See LICENSE file for license information.
"""Test subp.py."""

import subprocess
from unittest import mock

from whatsthis.subp import execute


@mock.patch.object(subprocess, 'Popen')
def test_execute(m_popen):
    """Return True when systemd-detect virt exits success."""
    mock_communicate_method = mock.MagicMock()
    mock_communicate_method.return_value = (b'my_file', b'')

    process_mock = mock.MagicMock()
    process_mock.communicate = mock_communicate_method
    process_mock.returncode = 0
    m_popen.return_value = process_mock

    result = execute(['ls'])

    assert result == 'my_file'
    assert result.stderr == ''
    assert result.return_code == 0
    assert bool(result)
    assert result.ok
    assert not result.failed


@mock.patch.object(subprocess, 'Popen')
def test_execute_string(m_popen):
    """Return True when systemd-detect virt exits success."""
    mock_communicate_method = mock.MagicMock()
    mock_communicate_method.return_value = (b'my_file', b'')

    process_mock = mock.MagicMock()
    process_mock.communicate = mock_communicate_method
    process_mock.returncode = 0
    m_popen.return_value = process_mock

    result = execute('ls')

    assert result == 'my_file'
    assert result.stderr == ''
    assert result.return_code == 0
    assert bool(result)
    assert result.ok
    assert not result.failed


@mock.patch.object(subprocess, 'Popen')
def test_execute_badcmd(m_popen):
    """Return True when systemd-detect virt exits success."""
    mock_communicate_method = mock.MagicMock()
    mock_communicate_method.return_value = (b'', b'Command not found')

    process_mock = mock.MagicMock()
    process_mock.communicate = mock_communicate_method
    process_mock.returncode = 1
    m_popen.return_value = process_mock

    result = execute('fake_cmd')

    assert result == ''
    assert result.stderr == 'Command not found'
    assert result.return_code == 1
    assert not bool(result)
    assert not result.ok
    assert result.failed
