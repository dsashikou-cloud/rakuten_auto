name: Test Threads Post

on:
  workflow_dispatch:

jobs:
  post:
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: Checkout
        uses: actions/checkout@v5

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install requests
        run: pip install requests==2.32.3

      - name: Post test text to Threads
        env:
          THREADS_ACCESS_TOKEN: ${{ secrets.THREADS_ACCESS_TOKEN }}
        run: python post_test.py
