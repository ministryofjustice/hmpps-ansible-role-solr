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


## Testing 

The role can be tested using Python molecule:

Install deps from the requirements.txt file and provide AWS credentials

```
export AWS_ACCESS_KEY_ID=ASIA****
export AWS_SECRET_ACCESS_KEY=9gPqlV3R****
export AWS_SESSION_TOKEN=FwoGZXIvYXdzE****
export AWS_DEFAULT_REGION=eu-west-2
```

```
molecule test -s aws
```


License
-------

MIT

Author Information
------------------

authors:
  - HMPPS
