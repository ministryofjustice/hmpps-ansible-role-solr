import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

solr_base_dir = "/opt/solr/alfresco-search-services"
solr_rerank_conf_dir = f"{solr_base_dir}/data/solrhome/templates/rerank/conf"


def test_mountpoint_present(host):

    mount_point = f"{solr_base_dir}/data"
    assert host.mount_point(mount_point).exists
    assert host.mount_point(mount_point).filesystem == "xfs"


@pytest.mark.parametrize("svc", [
    ("solr"),
    ("logstash"),
    ("chronyd")
])
def test_services_are_enabled(host, svc):
    service = host.service(svc)
    assert service.is_enabled
    assert service.is_running


@pytest.mark.parametrize("port", [
    (8983),
    (22),
    ("5044"),
    ("9600")
])
def test_service_ports_are_listening(host, port):
    assert host.socket(f"tcp://0.0.0.0:{port}")


@pytest.mark.parametrize("cron_task", [
    ("solr_backup"),
])
def test_solr_backup_cron_is_present(host, cron_task):
    assert host.ansible("cron", f"name={cron_task}state=present", become=True)


@pytest.mark.parametrize("user_id, user_group, user_dir", [
    ("solr", "solr", f"{solr_base_dir}/data/solrhome/alfresco"),
    ("solr", "solr", f"{solr_base_dir}/data/solrhome/archive"),
])
def test_application_directories_exist(host, user_id, user_group, user_dir):
    f = host.file(user_dir)
    assert f.is_directory
    assert f.user == user_id
    assert f.group == user_group


@pytest.mark.parametrize("user_id, user_group, file_name", [
    (
        "solr",
        "solr",
        f"{solr_rerank_conf_dir}/solrcore.properties"
    ),
    ("solr", "solr", "/etc/default/solr.in.sh"),
    ("root", "root", "/root/solr_backup.sh"),
])
def test_application_files_exist(host, user_id, user_group, file_name):
    f = host.file(file_name)
    assert f.is_file
    assert f.user == user_id
    assert f.group == user_group
