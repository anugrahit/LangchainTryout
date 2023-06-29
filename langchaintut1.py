# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b46a2db2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Downloading streamlit-1.24.0-py2.py3-none-any.whl (8.9 MB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m8.9/8.9 MB\u001b[0m \u001b[31m2.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hCollecting openai\n",
      "  Downloading openai-0.27.8-py3-none-any.whl (73 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m73.6/73.6 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting langchain\n",
      "  Downloading langchain-0.0.216-py3-none-any.whl (1.1 MB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m1.1/1.1 MB\u001b[0m \u001b[31m4.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hCollecting blinker<2,>=1.0.0\n",
      "  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)\n",
      "Collecting pympler<2,>=0.9\n",
      "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m3.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: packaging<24,>=14.1 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (22.0)\n",
      "Collecting gitpython!=3.1.19,<4,>=3\n",
      "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m184.3/184.3 kB\u001b[0m \u001b[31m5.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: typing-extensions<5,>=4.0.1 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (4.4.0)\n",
      "Collecting tzlocal<5,>=1.1\n",
      "  Downloading tzlocal-4.3.1-py3-none-any.whl (20 kB)\n",
      "Requirement already satisfied: pillow<10,>=6.2.0 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (9.4.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (4.22.4)\n",
      "Requirement already satisfied: pandas<3,>=0.25 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (1.5.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (8.0.4)\n",
      "Collecting pydeck<1,>=0.1.dev5\n",
      "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m3.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: importlib-metadata<7,>=1.4 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (4.11.3)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.0.0 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (8.0.1)\n",
      "Collecting validators<1,>=0.2\n",
      "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
      "  Preparing metadata (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25hCollecting rich<14,>=10.11.0\n",
      "  Downloading rich-13.4.2-py3-none-any.whl (239 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m239.4/239.4 kB\u001b[0m \u001b[31m3.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hCollecting pyarrow>=4.0\n",
      "  Downloading pyarrow-12.0.1-cp310-cp310-macosx_10_14_x86_64.whl (24.7 MB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m24.7/24.7 MB\u001b[0m \u001b[31m2.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hCollecting altair<6,>=4.0\n",
      "  Downloading altair-5.0.1-py3-none-any.whl (471 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m471.5/471.5 kB\u001b[0m \u001b[31m2.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: toml<2 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: python-dateutil<3,>=2 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.4 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (2.28.1)\n",
      "Requirement already satisfied: numpy<2,>=1 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (1.23.5)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in ./anaconda3/lib/python3.10/site-packages (from streamlit) (5.3.0)\n",
      "Collecting aiohttp\n",
      "  Downloading aiohttp-3.8.4-cp310-cp310-macosx_10_9_x86_64.whl (358 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m358.1/358.1 kB\u001b[0m \u001b[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: tqdm in ./anaconda3/lib/python3.10/site-packages (from openai) (4.64.1)\n",
      "Requirement already satisfied: numexpr<3.0.0,>=2.8.4 in ./anaconda3/lib/python3.10/site-packages (from langchain) (2.8.4)\n",
      "Collecting tenacity<9,>=8.0.0\n",
      "  Downloading tenacity-8.2.2-py3-none-any.whl (24 kB)\n",
      "Collecting openapi-schema-pydantic<2.0,>=1.2\n",
      "  Downloading openapi_schema_pydantic-1.2.4-py3-none-any.whl (90 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m90.0/90.0 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: PyYAML>=5.4.1 in ./anaconda3/lib/python3.10/site-packages (from langchain) (6.0)\n",
      "Collecting pydantic<2,>=1\n",
      "  Downloading pydantic-1.10.9-cp310-cp310-macosx_10_9_x86_64.whl (2.9 MB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m2.9/2.9 MB\u001b[0m \u001b[31m2.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hCollecting langchainplus-sdk>=0.0.17\n",
      "  Downloading langchainplus_sdk-0.0.17-py3-none-any.whl (25 kB)\n",
      "Collecting async-timeout<5.0.0,>=4.0.0\n",
      "  Downloading async_timeout-4.0.2-py3-none-any.whl (5.8 kB)\n",
      "Collecting dataclasses-json<0.6.0,>=0.5.7\n",
      "  Downloading dataclasses_json-0.5.8-py3-none-any.whl (26 kB)\n",
      "Requirement already satisfied: SQLAlchemy<3,>=1.4 in ./anaconda3/lib/python3.10/site-packages (from langchain) (1.4.39)\n",
      "Collecting yarl<2.0,>=1.0\n",
      "  Downloading yarl-1.9.2-cp310-cp310-macosx_10_9_x86_64.whl (65 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m65.7/65.7 kB\u001b[0m \u001b[31m1.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: attrs>=17.3.0 in ./anaconda3/lib/python3.10/site-packages (from aiohttp->openai) (22.1.0)\n",
      "Requirement already satisfied: charset-normalizer<4.0,>=2.0 in ./anaconda3/lib/python3.10/site-packages (from aiohttp->openai) (2.0.4)\n",
      "Collecting frozenlist>=1.1.1\n",
      "  Downloading frozenlist-1.3.3-cp310-cp310-macosx_10_9_x86_64.whl (35 kB)\n",
      "Collecting multidict<7.0,>=4.5\n",
      "  Downloading multidict-6.0.4-cp310-cp310-macosx_10_9_x86_64.whl (29 kB)\n",
      "Collecting aiosignal>=1.1.2\n",
      "  Downloading aiosignal-1.3.1-py3-none-any.whl (7.6 kB)\n",
      "Requirement already satisfied: toolz in ./anaconda3/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: jinja2 in ./anaconda3/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in ./anaconda3/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Collecting marshmallow<4.0.0,>=3.3.0\n",
      "  Downloading marshmallow-3.19.0-py3-none-any.whl (49 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m49.1/49.1 kB\u001b[0m \u001b[31m1.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting typing-inspect>=0.4.0\n",
      "  Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
      "Collecting marshmallow-enum<2.0.0,>=1.5.1\n",
      "  Downloading marshmallow_enum-1.5.1-py2.py3-none-any.whl (4.2 kB)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: zipp>=0.5 in ./anaconda3/lib/python3.10/site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.11.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in ./anaconda3/lib/python3.10/site-packages (from pandas<3,>=0.25->streamlit) (2022.7)\n",
      "Requirement already satisfied: six>=1.5 in ./anaconda3/lib/python3.10/site-packages (from python-dateutil<3,>=2->streamlit) (1.16.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in ./anaconda3/lib/python3.10/site-packages (from requests<3,>=2.4->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./anaconda3/lib/python3.10/site-packages (from requests<3,>=2.4->streamlit) (1.26.14)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.10/site-packages (from requests<3,>=2.4->streamlit) (2023.5.7)\n",
      "Collecting markdown-it-py>=2.2.0\n",
      "  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m87.5/87.5 kB\u001b[0m \u001b[31m2.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting pygments<3.0.0,>=2.13.0\n",
      "  Downloading Pygments-2.15.1-py3-none-any.whl (1.1 MB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m1.1/1.1 MB\u001b[0m \u001b[31m3.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: greenlet!=0.4.17 in ./anaconda3/lib/python3.10/site-packages (from SQLAlchemy<3,>=1.4->langchain) (2.0.2)\n",
      "Collecting pytz-deprecation-shim\n",
      "  Downloading pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\n",
      "Requirement already satisfied: decorator>=3.4.0 in ./anaconda3/lib/python3.10/site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in ./anaconda3/lib/python3.10/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in ./anaconda3/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Collecting mdurl~=0.1\n",
      "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Requirement already satisfied: mypy-extensions>=0.3.0 in ./anaconda3/lib/python3.10/site-packages (from typing-inspect>=0.4.0->dataclasses-json<0.6.0,>=0.5.7->langchain) (0.4.3)\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)\n",
      "\u001b[2K     \u001b[90mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\u001b[0m \u001b[32m341.8/341.8 kB\u001b[0m \u001b[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hBuilding wheels for collected packages: validators\n",
      "  Building wheel for validators (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19581 sha256=258b380becdd34185d785113e1933c0389870bf37a2acd841b70ee043b9d5c07\n",
      "  Stored in directory: /Users/Anugrahit/Library/Caches/pip/wheels/2d/55/25/123071088f4e466746cbadc923b1a31e08cea99ea9ef6bb35e\n",
      "Successfully built validators\n",
      "Installing collected packages: validators, tzdata, typing-inspect, tenacity, smmap, pympler, pygments, pydantic, pyarrow, multidict, mdurl, marshmallow, frozenlist, blinker, async-timeout, yarl, pytz-deprecation-shim, pydeck, openapi-schema-pydantic, marshmallow-enum, markdown-it-py, langchainplus-sdk, gitdb, aiosignal, tzlocal, rich, gitpython, dataclasses-json, altair, aiohttp, streamlit, openai, langchain\n",
      "  Attempting uninstall: tenacity\n",
      "    Found existing installation: tenacity 8.0.1\n",
      "    Uninstalling tenacity-8.0.1:\n",
      "      Successfully uninstalled tenacity-8.0.1\n",
      "  Attempting uninstall: pygments\n",
      "    Found existing installation: Pygments 2.11.2\n",
      "    Uninstalling Pygments-2.11.2:\n",
      "      Successfully uninstalled Pygments-2.11.2\n",
      "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "spyder 5.4.1 requires pyqt5<5.16, which is not installed.\n",
      "spyder 5.4.1 requires pyqtwebengine<5.16, which is not installed.\u001b[0m\u001b[31m\n",
      "\u001b[0mSuccessfully installed aiohttp-3.8.4 aiosignal-1.3.1 altair-5.0.1 async-timeout-4.0.2 blinker-1.6.2 dataclasses-json-0.5.8 frozenlist-1.3.3 gitdb-4.0.10 gitpython-3.1.31 langchain-0.0.216 langchainplus-sdk-0.0.17 markdown-it-py-3.0.0 marshmallow-3.19.0 marshmallow-enum-1.5.1 mdurl-0.1.2 multidict-6.0.4 openai-0.27.8 openapi-schema-pydantic-1.2.4 pyarrow-12.0.1 pydantic-1.10.9 pydeck-0.8.1b0 pygments-2.15.1 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 rich-13.4.2 smmap-5.0.0 streamlit-1.24.0 tenacity-8.2.2 typing-inspect-0.9.0 tzdata-2023.3 tzlocal-4.3.1 validators-0.20.0 yarl-1.9.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit openai langchain "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "baac5745",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from langchain.llms import OpenAI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "21a6eaa2",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title('ðŸ¦œðŸ”— Quickstart App')\n",
    "\n",
    "openai_api_key = st.sidebar.text_input('Add API Key')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "24195ae2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def generate_response(input_text):\n",
    "  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)\n",
    "  st.info(llm(input_text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "87947670",
   "metadata": {},
   "outputs": [],
   "source": [
    "with st.form('my_form'):\n",
    "  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')\n",
    "  submitted = st.form_submit_button('Submit')\n",
    "  if not openai_api_key.startswith('sk-'):\n",
    "    st.warning('Please enter your OpenAI API key!', icon='âš ')\n",
    "  if submitted and openai_api_key.startswith('sk-'):\n",
    "    generate_response(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "",
   "id": "fec669d7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}