mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
base='light'\n\
backgroundColor='#efe1b2'\n\
secondaryBackgroundColor='#edf2f9'\n\
" > ~/.streamlit/config.toml
