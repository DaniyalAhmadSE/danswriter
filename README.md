# danswriter
danswriter is an app to create posts for your blogspot by leveraging GPT and PaLM. None of the requirements need to be paid for as of now (Oct 2nd, 2023).

## Features
* Write posts for your blogspot (with labels/tags) using:
  * GPT-3.5 via [tgpt](https://github.com/DaniyalAhmadSE/danswriter#about-tgpt)
  * PaLM 2 via the official API
* Insert images from Unsplash using the official API
* Upload your post on Blogger using the official API
  * Built-in bearer token refresh (using OAuth flow)

## Pre-requisites
1. Either the official API keys for PaLM 2 OR [tgpt](https://github.com/DaniyalAhmadSE/danswriter#about-tgpt) installed on your machine. 
2. Unsplash API key (If you do not want to get the API key and are fine without having pictures in your post, then you can comment out the relevant code.)
3. The official Blogger API key.

## Installation
To install this project, follow these steps:
1. Clone the repository:
```
git clone https://github.com/DaniyalAhmadSE/danswriter.git
```
2. Install the dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Configure the app from the [config.json](https://github.com/DaniyalAhmadSE/danswriter/blob/main/config.json) file. Refer to the [help.json](https://github.com/DaniyalAhmadSE/danswriter/blob/main/help.json) file for details.
2. Run app.py from your favorite IDE or with:
```
python app.py
```

## Contributing
To contribute to this project, follow these steps:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

## License
This project is licensed under the **[MIT](https://github.com/DaniyalAhmadSE/danswriter/blob/main/LICENSE.md)** license.

## Contact
For questions or suggestions (especially regarding prompts), contact me at daniyalahmad.se@gmail.com.

### Additional information

* **Roadmap:**
  * Improve the prompt.
  * Integrate an improved PaLM model.
  * Allow integration of GPT using the official Openai API keys.
  * Integrate more blogging sites.

* **Contributors:**
  * Just [me](https://github.com/DaniyalAhmadSE) for now :)

* **Official Blogspot:**
  * Read the official blogs written by danswriter at [danswriter.blogspot.com](https://danswriter.blogspot.com)

* #### About tgpt
  * [tgpt](https://github.com/aandrew-me/tgpt) by [aandrew-me](https://github.com/aandrew-me) is an awesome cross-platform ChatGPT CLI client that does not require Openai API keys. Follow the [official installation instructions](https://github.com/aandrew-me/tgpt#installation-) for tgpt.
