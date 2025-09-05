module.exports = {
 apps: [
    {
        name: "main",
        script: "/bots/iki_bot/main.py",
        interpreter: "/bots/iki_bot/venv/bin/python",
        env: {
            PYTHONPATH: "/bots/iki_bot/venv/bin/python",
            PATH: "/bots/iki_bot/venv/bin:$PATH"
        }
    }
 ]
};
