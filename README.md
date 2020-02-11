Solr installation
=========

## Summary

This role:
  - Installs Solr standalone on Centos 7.

Requirements
------------
  - Minimal Version of the ansible for installation: 2.8
  - **Supported OS**:
    - CentOS
      - 7

## Role Variables
  - `solr_version` - matches available version on https://archive.apache.org/dist/lucene/solr/. Tested versions 8.x

    default: `8.4.1`

  - `solr_use_java_version_8` - if True Solr installed on java version 8 and earlier. If using later versions - set to False

    default: `True`

  - `solr_url` - root url to download solr

    default: `http://archive.apache.org/dist/lucene/solr`

  - `solr_distr_url` - url to tgz file

    default: `{{ solr_url }}/{{ solr_version }}/solr-{{ solr_version }}.tgz`

  - `solr_host` - solr server name

    default: `{{ ansible_fqdn }}`

  - `solr_dest_main_path` - root directory to store solr folder

    default: `/opt` for Linux OS

  - `solr_dest_path` - solr folder path

    default: `{{ solr_dest_main_path }}/solr-{{ solr_version }}`

  - `solr_change_default_password` - to change default password to solr user (will be solr_auth_pass)

    default: `True`

  - `solr_auth_configure` - Enable authentication

    default: `True`

  - `solr_auth_type` - authentication type

    default: `basic`

  - `solr_auth_user` - default solr user

    default: `solrserver`

  - `solr_auth_pass` - default solr user password

    default: `server123`

  - `solr_default_auth_user` - default solr user

    default: `solr`

  - `solr_default_auth_pass` - default solr user password

    default: `SolrRocks`

  - `solr_authentication_opts` - solr authentication options

    default: `-Dbasicauth={{ solr_auth_user }}:{{ solr_auth_pass }}`

  - `solr_insh_default` - solr in.sh folder

    default: `/etc/default/solr.in.sh`

  - `solr_java_xms` - heap size

    default: `512m`

  - `solr_java_xmx` - heap size

    default: `512m`

  - `solr_master_enable_jmx` - enable jmx on solr

    default: `false`

  - `solr_additional_opts` - solr options

    default: `-Xss256k`

  - `solr_user` - os user to run solr service

    default: `solr`

  - `solr_group` - os group for user

    default: `solr`

  - `solr_port` - port for solr start

    default: `8983`

  - `solr_service_name` - solr service name

    default: `solr`

  - `solr_base_path` - path to solr base

    default: `/var/solr`

  - `solr_home` - path to SOLR_HOME

    default: `{{ solr_base_path }}/data`

  - `solr_with_systemd` - to run solr as a service

    default: `True`

  - `solr_logs_dir` - path to store logs

    default: `{{ solr_base_path }}/logs`

  - `solr_wait_for_zk` - timeout to reconnect to zookeeper (in seconds)

    default: `30`

  - `solr_client_timeout` - ZooKeeper client timeout (for SolrCloud mode)

    default: `15000`

  - `solr_timezone` - timezone for solr server

    default: `UTC`

  - `solr_service_restart` - solr service restart option

    default: `always`

  - `solr_service_start` - to start solr service in the end of role/Playbook

    default: `True`

  - `solr_service_autostart` - Add solr service to automatically start.

    default: `True`

  - `solr_copy_default_configsets` - copy OOTB configsets to {{ solr_home }}/configsets folder

    default: False

# https://lucene.apache.org/solr/guide/8_4/enabling-ssl.html
  - `solr_local_keystore` - if True - to search for keystore on ansible host on {{ solr_local_keystore_path }}. If False - to check keystore on remote host

    default: `True`

  - `solr_local_keystore_path` - path to local keystore file (in order not to create self-signed)

    default: `{{ role_path }}/files/{{ solr_ssl_key_store_name }}`

  - `solr_ssl_configure` - configure SSL

    default: `True`

  - `solr_ssl_key_size` - certificate key size

    default: 4096

  - `solr_ssl_key_store_path` - directory to store keystore

    default: `{{ solr_dest_path }}/server/solr`

  - `solr_ssl_key_store_name` - keystore name. If file with such name exists in role folder/files - it will be used as keystore.

    default: `solr-ssl.keystore.jks`

  - `solr_ssl_key_store` - path to solr keystore.

    default: `{{ solr_ssl_key_store_path }}/{{ solr_ssl_key_store_name }}`

  - `solr_ssl_key_store_password` - keystore password

    default: `123456`

  - `solr_ssl_trust_store` - path to trust keystore

    default: `{{ solr_ssl_key_store_path }}/{{ solr_ssl_key_store_name }}`

  - `solr_ssl_trust_store_password` - trusted keystore password

    default: `123456`

  - `solr_ssl_need_client_auth` - Client Authentication Settings

    default: `false`

  - `solr_ssl_want_client_auth` - Client Authentication Settings

    default: `false`

  - `solr_ssl_key_store_type` - keystore type

    default: `JKS`

  - `solr_ssl_trust_store_type` - trusted keystore path

    default: `JKS`

  - `solr_ssl_check_peer_name` - Setting this to false can be useful to disable these checks when re-using a certificate on many hosts

    default: `true`

  - `solr_ssl_certificate_provider` - only for Linux os. https://docs.ansible.com/ansible/latest/openssl_certificate_module.html

    default: `selfsigned`

  - `solr_ca_domain` - certificate domain name

    default: `example.com`

  - `local_cert_file_path` - path to private cert

    default: `/etc/pki/tls/private` for RHEL based

    default: `/etc/ssl/private` for Debian based

  - `solr_local_pkey_file_name` - private cert name

    default: `{{ ansible_hostname }}.ca-pkey.pem`

  - `local_cert_file_path` - path to public cert

    default: `/etc/pki/tls/certs` for RHEL based

    default: `/etc/ssl/certs` for Debian based

  - `solr_local_cert_file_name` -public cert name

    default: `{{ ansible_hostname }}.ca-cert.pem`

  - `solr_set_limits` - to set limits

    default: `True`

  - `solr_open_files_limit` - linux open files limit value

    default: `65000`

  - `solr_max_processes_limit` - linux max processes limit value

    default: `65000`

Example Playbook
----------------

```yml
- name: Install and Configure Solr
  hosts: localhost
```

License
-------

MIT

Author Information
------------------

authors:
  - HMPPS
