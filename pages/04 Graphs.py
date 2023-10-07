import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tableau Connections", page_icon=":bar_chart:", layout="wide")
# Everyone should insert their code of Tableau in here to make it Unique! The tableau Temp should be inside a main function:
st.title ("YES, it is possible to link streamlit to Tableau")
st.header("You may also interact with your Tableau Public repos, just like this: ")
def main():
    html_temp='''<div class='tableauPlaceholder' id='viz1695773550460' style='position: relative'><noscript><a href='#'><img alt='Tarantino Analysis ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ta&#47;Tarantino_16775583352980&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Tarantino_16775583352980&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ta&#47;Tarantino_16775583352980&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1695773550460');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1016px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
    components.html(html_temp, width=1000, height=600)

if __name__ == '__main__':
    main()