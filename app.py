import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="CE-Advisor – EN 60335 & RED",
    page_icon="🏷️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit chrome komplett ausblenden für nahtlose Darstellung
st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    .stApp { margin: 0; padding: 0; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

html_content = Path("ce-advisor.html").read_text(encoding="utf-8")

# Höhe dynamisch per JS anpassen: iframe sendet eigene Höhe an Streamlit-Parent
resize_script = """
<script>
  window.addEventListener('load', function() {
    function sendHeight() {
      const h = document.body.scrollHeight;
      window.parent.postMessage({ type: 'streamlit:setFrameHeight', height: h }, '*');
    }
    sendHeight();
    new MutationObserver(sendHeight).observe(document.body, { childList: true, subtree: true, attributes: true });
  });
</script>
"""

# Script vor </body> einfügen
html_with_resize = html_content.replace("</body>", resize_script + "\n</body>")

st.components.v1.html(html_with_resize, height=3200, scrolling=True)
