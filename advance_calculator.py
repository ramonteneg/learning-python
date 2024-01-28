{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ramonteneg/learning-python/blob/main/advance_calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "os.system('clear')\n",
        "\n",
        "#inputs\n",
        "print(\"Ingrese primer valor: \")\n",
        "n1 = int(input())\n",
        "n2 = int(input(\"Ingrese el segundo valor: \\n\"))\n",
        "suma = n1 + n2\n",
        "print(\"Suma:\", suma)\n",
        "\n",
        "print(type(n1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yrQew2Ge_jbL",
        "outputId": "a24cc498-00fb-4958-8868-831887986494"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese primer valor: \n",
            "1\n",
            "Ingrese el segundo valor: \n",
            "3\n",
            "Suma: 4\n",
            "<class 'int'>\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMfbfDoIOhOTzwwpfukOCZW",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}