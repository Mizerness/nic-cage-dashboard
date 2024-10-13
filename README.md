<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlvNgetEBhUikAQS1CPYOE1qjsjhlSCFH8mA&s" width="60%" alt="NIC-CAGE-DASHBOARD-logo">
</p>
<p align="center">
    <h1 align="center">NICOLAS CAGE DASHBOARD</h1>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Mizerness/nic-cage-dashboard?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Mizerness/nic-cage-dashboard?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Mizerness/nic-cage-dashboard?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Mizerness/nic-cage-dashboard?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=flat&logo=Plotly&logoColor=white" alt="Plotly">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
</p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔖 Prerequisites](#-prerequisites)
  - [📦 Installation](#-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<p>This Streamlit app provides you with a detailed tour of Nicolas Cage's brilliant film career. Through three different pages, you can learn more about the GOAT of cinema.</p>
<p>You can find a demo <a href="https://nicolas-cage-dashboard.streamlit.app/">here</a>.</p>

---

## 👾 Features

- **Exploratory Analysis**: Dive into the dataset we're using for this app, with insights and clean data preparation explained in the code.
- **Career Overview**: A deep dive into Nicolas Cage's career highlights, along with some fun and surprising insights.
- **Nic Cage vs. The World**: Compare Nicolas Cage's career with other actors and see how he stacks up in this fun face-off!

---

## 📂 Repository Structure

```sh
└── nic-cage-dashboard/
    ├── cleaning
    │   ├── 1_eda.py
    │   ├── 1b_eda_results.py
    │   ├── 2_clean.py
    │   └── test.py
    ├── data
    │   ├── eda_results.csv
    │   ├── imdb-movies-cleaned.csv
    │   └── imdb-movies-dataset.csv
    ├── pages
    │   ├── 1_🔍_Exploratory_analysis.py
    │   ├── 2_📈_His_career.py
    │   └── 3_🌍_Nic_Cage_vs__The_World.py
    ├── requirements.txt
    ├── utils
    │   └── utils.py
    └── 🏠_Home.py
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                           | Summary                                      |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [🏠_Home.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/🏠_Home.py)             | <code>Eq. of main.py</code>                  |
| [requirements.txt](https://github.com/Mizerness/nic-cage-dashboard/blob/main/requirements.txt) | <code>The dependencies to run the app</code> |

</details>

<details closed><summary>cleaning</summary>

| File                                                                                                      | Summary                                                                     |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [1_eda.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/cleaning/1_eda.py)                   | <code>Exploratory analysis of the dataset</code>                            |
| [1b_eda_results.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/cleaning/1b_eda_results.py) | <code>Generation of eda results</code>                                      |
| [test.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/cleaning/test.py)                     | <code>Random file [to be deleted]</code>                                    |
| [2_clean.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/cleaning/2_clean.py)               | <code>Cleaning the dataset [error in the numbers, happen before eda]</code> |

</details>

<details closed><summary>pages</summary>

| File                                                                                                                               | Summary             |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| [1_🔍_Exploratory_analysis.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/pages/1_🔍_Exploratory_analysis.py)       | <code>Page 1</code> |
| [3_🌍_Nic_Cage_vs\_\_The_World.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/pages/3_🌍_Nic_Cage_vs__The_World.py) | <code>Page 2</code> |
| [2_📈_His_career.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/pages/2_📈_His_career.py)                           | <code>Page 3</code> |

</details>

<details closed><summary>utils</summary>

| File                                                                                 | Summary                         |
| ------------------------------------------------------------------------------------ | ------------------------------- |
| [utils.py](https://github.com/Mizerness/nic-cage-dashboard/blob/main/utils/utils.py) | <code>❯ Useful functions</code> |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version 3.12.2`

### 📦 Installation

Build the project from source:

1. Clone the nic-cage-dashboard repository:

```sh
❯ git clone https://github.com/Mizerness/nic-cage-dashboard
```

2. Navigate to the project directory:

```sh
❯ cd nic-cage-dashboard
```

3. Install the required dependencies:

```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ streamlit run Hain.py
```

## 📌 Project Roadmap

- [ ] Clean the code
- [ ] More data to do geospatial analysis
- [ ] Realtime actor fight with betting game
- [ ] AI chat to discuss directly with Nicolas Cage

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Mizerness/nic-cage-dashboard/issues)**: Submit bugs found or log feature requests for the `nic-cage-dashboard` project.
- **[Submit Pull Requests](https://github.com/Mizerness/nic-cage-dashboard/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Mizerness/nic-cage-dashboard/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Mizerness/nic-cage-dashboard
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Mizerness/nic-cage-dashboard/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Mizerness/nic-cage-dashboard">
   </a>
</p>
</details>
