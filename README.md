# Creating job descriptions using Generative AI

[![License: UPL](https://img.shields.io/badge/license-UPL-green)](https://img.shields.io/badge/license-UPL-green)<!--[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=oracle-devrel_competency-development-genai)](https://sonarcloud.io/dashboard?id=oracle-devrel_competency-development-genai)-->

## Introduction

As a recruiter or hiring manager, you can use AI assistance to create the first draft of a *job description* based on job title, company, and division.

The Generative AI component can assist creating a draft job description that includes a summary, description, responsibilities, and qualifications.

This is a demo solution showcasing how you can use OCI Generative AI service to quickly create a working application.

The application has the following components:

- OCI Generative AI Service to run Large Language Model (LLM) generations
- Streamlit framework as the front-end, to allow users to interact with the LLM
- Python environment to run the code, either locally or on OCI

## 0. Prerequisites and setup

### Prerequisites

- An Oracle Cloud Infrastructure (OCI) Account
- [OCI SDK](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)

Follow these links below to generate a config file and a key pair in your ~/.oci directory:

[SDK Config](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)
[API Signing Key](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm)
[SDK CLI Installation](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#configfile)

After completion, you should have following 2 things in your `~/.oci` directory:

- A config file(where key file point to private key:key_file=~/.oci/oci_api_key.pem)
- A key pair named `oci_api_key.pem` and `oci_api_key_public.pem`
- Now, make sure you change the reference of key file in config file (where key file point to private key:key_file=/YOUR_DIR_TO_KEY_FILE/oci_api_key.pem)

## 1. Getting started

Application uses OCI Generative AI Service to create Job Description based on user inputs. The OCI client ```client.py``` creates the client to connect to the OCI Generative AI service.

To install the demo application, follow the steps below:

1. Update the `config.toml` file with location of your oci config file:

    ```toml
    [user]
    userconfig = <you OCI config file location>
    profile = "DEFAULT"
    compartment_id = <Your compartment OCID>
    ```

    > By default, the installation path is `~/.oci/config`.

2. If you don't have a virtual environment, create a new one:

    ```bash
    python3 -m venv .demo
    ```

3. Activate the virtual environment you just created:

    ```bash
    source .demo/bin/activate
    ```

4. Install Python requirements into the environment:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the app:

  ```bash
  (.demo) %  streamlit run jobposting.py
  ```

This should spin up the application and the following message will be displayed in the terminal:

```bash
  > You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.126.180.172:8501
```

> You can access the application in your browser, using either localhost for deploying locally or hosting it in an OCI Compute Instance and exposing its public IP address to the Internet.

![streamlit interface](img/image.png)

Feel free to experiment with the prompt and some examples. Enjoy!

## Contributing

<!-- If your project has specific contribution requirements, update the
    CONTRIBUTING.md file to ensure those requirements are clearly explained. -->

This project welcomes contributions from the community. Before submitting a pull
request, please [review our contribution guide](./CONTRIBUTING.md).

## Security

Please consult the [security guide](./SECURITY.md) for our responsible security
vulnerability disclosure process.

## License

Copyright (c) 2024 Oracle and/or its affiliates.

Licensed under the Universal Permissive License (UPL), Version 1.0.

See [LICENSE](LICENSE.txt) for more details.

ORACLE AND ITS AFFILIATES DO NOT PROVIDE ANY WARRANTY WHATSOEVER, EXPRESS OR IMPLIED, FOR ANY SOFTWARE, MATERIAL OR CONTENT OF ANY KIND CONTAINED OR PRODUCED WITHIN THIS REPOSITORY, AND IN PARTICULAR SPECIFICALLY DISCLAIM ANY AND ALL IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.  FURTHERMORE, ORACLE AND ITS AFFILIATES DO NOT REPRESENT THAT ANY CUSTOMARY SECURITY REVIEW HAS BEEN PERFORMED WITH RESPECT TO ANY SOFTWARE, MATERIAL OR CONTENT CONTAINED OR PRODUCED WITHIN THIS REPOSITORY. IN ADDITION, AND WITHOUT LIMITING THE FOREGOING, THIRD PARTIES MAY HAVE POSTED SOFTWARE, MATERIAL OR CONTENT TO THIS REPOSITORY WITHOUT ANY REVIEW. USE AT YOUR OWN RISK.
