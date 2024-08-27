from bs4 import BeautifulSoup
import requests

# URL do site que você quer fazer o scraping
url = 'https://www.letras.mus.br/mais-acessadas/'  # Substitua com a URL real

# Fazer a requisição para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Levanta um erro se a requisição falhar

# Fazer o parsing do conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar o <ol> com a classe 'top-list_mus'
top_list_ol = soup.find('ol', class_='top-list_mus')

# Verificar se encontramos a lista
if top_list_ol:
    # Encontrar todos os <a> dentro dessa lista
    links = []
    for a_tag in top_list_ol.find_all('a', href=True):
        href = a_tag['href']
        links.append(href)

    # Exibir os links encontrados
    num = 1
    for link in links:
        print(f'https://www.letras.mus.br{link}')
        # https://www.letras.mus.br/grelo-da-seresta/so-fe/
else:
    print('A lista com a classe "top-list_mus" não foi encontrada.')


'''
<body class="pt-br" data-locale="pt-br" id="body">
  <script type="text/javascript">
   try{const matches=[...document.cookie.matchAll(/(lasub|lpsub)=([^;][A-Za-z0-9]{2,5})/g)];if(matches.length>0){document.body.classList.add("hasSubscription");for(const match of matches){if(match[1]=="lasub"){document.body.classList.add("hasSubscriptionAcademy");}if(match[1]=="lpsub"){document.body.classList.add("hasSubscriptionPremium");}}}}catch(e){}
  </script>
  <div class="wrapper">
   <header class="header">
    <div class="header-topBar">
     <div class="gridContainer --noMarginBottom">
      <div class="u-flex">
       <button class="header-menuButton">
        menu
       </button>
       <div class="header-logoContainer">
        <a class="header-logo" href="/">
         <h2>
          LETRAS.MUS.BR - Letras de músicas
         </h2>
        </a>
       </div>
      </div>
      <form class="header-search suggest">
       <label class="header-search-label">
        <input aria-label="O que você quer ouvir agora?" autocomplete="off" class="header-search-input font --base --strong --size16" id="main_suggest" placeholder="O que você quer ouvir agora?"/>
       </label>
       <button class="header-search-submit" title="buscar">
        buscar
       </button>
       <div class="suggest-drop modal">
        <ul class="suggest-list --mainSearch">
        </ul>
        <div class="suggest-all">
        </div>
       </div>
      </form>
      <div class="header-linksToLoggedUsers">
       <span id="js-user-send" style="display: none">
        <a class="font --base --strong --size16" data-ct-action="Nav Enviar Letra" data-ct-label="Barra (topo)" href="/contribuicoes/" rel="nofollow">
         <strong>
          Enviar letra
         </strong>
        </a>
       </span>
       <span id="js-user-menu">
       </span>
      </div>
     </div>
    </div>
    <div class="header-menus">
     <div class="gridContainer --noMarginBottom">
      <div class="menu modal" id="js-main-menu-modal">
       <div class="rail">
       </div>
       <div class="menu-tabs">
        <ul>
         <li>
          <a class="is-active" data-tab="menu-songs" href="/mais-acessadas/" id="js-music-tab">
           Músicas
          </a>
         </li>
         <li>
          <a data-tab="menu-artists" href="/mais-acessadas/">
           Artistas
          </a>
         </li>
         <li>
          <a data-tab="menu-musicalStyles" href="/estilos/">
           Estilos musicais
          </a>
         </li>
         <li>
          <a data-tab="menu-playlists" href="/playlists.html">
           Playlists
          </a>
         </li>
         <li>
          <a data-tab="menu-spotify" href="#">
           Spotify
          </a>
         </li>
         <li>
          <a data-tab="menu-dictionary" href="/academy/dicionario/">
           Treino de pronúncia
          </a>
         </li>
         <li>
          <a data-tab="menu-blog" href="/blog/">
           Blog
          </a>
         </li>
         <li>
          <a data-tab="menu-apps" href="#">
           Aplicativos
          </a>
         </li>
        </ul>
        <a data-ct-action="Nav Enviar Letra" data-ct-label="Menu (topo)" href="/contribuicoes/" rel="nofollow">
         Enviar letra
        </a>
       </div>
       <div class="menu-content menu-songs is-active" data-endpoint="songs">
       </div>
       <div class="menu-content menu-artists" data-endpoint="artists">
       </div>
       <div class="menu-content menu-musicalStyles" data-endpoint="genres">
       </div>
       <div class="menu-content menu-playlists" data-endpoint="playlists">
       </div>
       <div class="menu-content menu-spotify" data-endpoint="spotify" data-loaded="1">
        <div class="menu-spotify-content">
         <p class="menu-spotify-title font --base --size20">
          Busca rápida com Spotify
         </p>
         <p class="menu-spotify-description font --base --size14">
          Acompanhe as letras do que você está ouvindo.
         </p>
         <button class="menu-spotify-connect js-spotify-button">
          Conectar Spotify
         </button>
        </div>
       </div>
       <div class="menu-content menu-dictionary" data-endpoint="dictionary">
       </div>
       <div class="menu-content menu-blog" data-endpoint="blog">
       </div>
       <div class="menu-content menu-apps" data-endpoint="" data-loaded="1">
        <div class="menu-title font --base --size16">
         Aplicativos e plugins
        </div>
        <div class="menu-apps-mobile">
         <i>
          Mobile
         </i>
         <a class="menu-apps-playStore" href="https://play.google.com/store/apps/details?id=com.studiosol.player.letras" rel="noopener" target="_blank">
          Android
         </a>
         <a class="menu-apps-appStore" href="https://itunes.apple.com/br/app/letras.mus.br/id773347891?mt=8" rel="noopener" target="_blank">
          iPhone
         </a>
        </div>
        <div class="menu-apps-desktop">
         <i>
          Desktop
         </i>
         <a class="menu-apps-chrome" href="/plugin/chrome/">
          Google Chrome
         </a>
        </div>
       </div>
      </div>
      <div class="user modal" id="js-user-menu-modal">
       <div class="rail">
       </div>
       <div class="user-links">
        <ul class="user-links-list">
         <li>
          <a class="user-links-link font --base --size14" data-ga-label="meu-perfil" href="#" id="js-meu-perfil">
           Meu perfil
          </a>
         </li>
         <li>
          <a class="user-links-link font --base --size14" data-ct-action="Nav Enviar Letra" data-ct-label="Menu User (topo)" data-ga-label="enviar-letra" href="/contribuicoes/" rel="nofollow">
           Enviar letra
          </a>
         </li>
         <li>
          <a class="user-links-link font --base --size14" data-ga-label="mensagens" href="#" id="js-user-mensagens">
           Mensagens
          </a>
         </li>
         <li>
          <a class="user-links-link font --base --size14" data-ga-label="editar" href="https://accounts.letras.mus.br/editar/" rel="noopener" target="_blank">
           Editar
          </a>
         </li>
         <li class="user-localeDropdowns">
          <div class="user-selector" data-ga-label="local" id="region-selector">
           <label class="user-selector-label">
            <span>
             Local:
            </span>
            <button class="user-selector-button">
            </button>
           </label>
           <span class="user-selector-menu">
           </span>
          </div>
          <div class="user-selector" data-ga-label="idioma" id="language-selector">
           <label class="user-selector-label">
            <span>
             Idioma:
            </span>
            <button class="user-selector-button">
            </button>
           </label>
           <span class="user-selector-menu">
           </span>
          </div>
          <div class="user-selector" data-ga-label="tema" id="theme-selector">
           <label class="user-selector-label">
            <span>
             Tema:
            </span>
            <button class="user-selector-button">
            </button>
           </label>
           <span class="user-selector-menu">
           </span>
          </div>
         </li>
         <li>
          <a class="user-links-link font --base --size14" data-ga-label="sair" href="https://accounts.letras.mus.br/logout/" id="js-logout">
           Sair
          </a>
         </li>
        </ul>
       </div>
       <div class="user-wrapper">
        <div class="user-tabs filter">
         <div class="filter-tabs" id="user_tabs">
          <button class="chip --outline" data-ga-label="playlists" data-tab="user-playlists">
           <strong class="chip-label font --base --strong --size14">
            Playlists
           </strong>
          </button>
          <button class="chip --outline" data-ga-label="artistas" data-tab="user-artists">
           <strong class="chip-label font --base --strong --size14">
            Artistas
           </strong>
          </button>
          <button class="chip --outline" data-ga-label="albuns" data-tab="user-albums">
           <strong class="chip-label font --base --strong --size14">
            Álbuns
           </strong>
          </button>
          <button class="chip --outline" data-ga-label="notificacoes" data-tab="user-notifications">
           <strong class="chip-label font --base --strong --size14">
            Notificações
           </strong>
           <span class="js-n-n font">
           </span>
          </button>
          <button class="chip --outline" data-ga-label="amigos" data-tab="user-friends">
           <strong class="chip-label font --base --strong --size14">
            Amigos pendentes
           </strong>
           <span class="js-fr-n font">
           </span>
          </button>
         </div>
        </div>
        <div class="user-content user-playlists" data-endpoint="playlists">
         <div class="user-playlists-list on ps">
          <ul class="player-list user-playlists-default --owner" id="ccid_playlist-list">
          </ul>
         </div>
         <div class="user-playlistSongs-list ps">
          <div class="user-playlistSongs-header" id="js-playlist-header">
           <button class="user-playlistSongs-return" id="js-playlist-return">
            Voltar
           </button>
           <b class="user-playlistSongs-title font --base --strong --size20">
           </b>
           <button class="user-playlists-listen button --listen" data-title="Ouvir" id="js-user-menu-listen">
            Ouvir
           </button>
          </div>
          <ul class="player-list hasCounterReset playlistSongs-items" id="ccid_playlist-view">
          </ul>
         </div>
        </div>
        <div class="user-content user-artists" data-endpoint="artists">
        </div>
        <div class="user-content user-albums" data-endpoint="albums">
        </div>
        <div class="user-content user-notifications" data-endpoint="notifications">
         <div class="ps">
          <ul class="js-nt-list user-notifications-list">
          </ul>
         </div>
        </div>
        <div class="user-content user-friends" data-endpoint="friends">
         <div class="ps js-fr-not">
          <ul class="list ccid_notify_am">
          </ul>
         </div>
        </div>
       </div>
      </div>
      <script id="user_widget_send_template" type="text/template">
       <a rel="nofollow" href="/contribuicoes/">Enviar letra</a>
      </script>
      <script id="user_widget_template" type="text/template">
       <a class="js-user-open-login font --base --strong --size16" href="#" data-ga-label="entrar">Entrar</a>
      </script>
      <script id="user_widget_auth_template" type="text/template">
       <a href="/membros/%id%/" class="header-user" data-ga-label="usuario"> <span class="font --base --size16 --strong">%nickname%</span>















<div class="thumbnail --skin-image --shape-circle --size-xSmall --tabletSize-xSmall">
    <img

            src="%avatar%"


        alt="%nickname%"





    >
</div> <i class="unreadNotifications" style="display:none" alt=""></i> </a>
      </script>
      <script id="notification_fr_template" type="text/template">
       <li data-userid="%userID%" data-id="%id%" class="%className%" > <a class="js-user-notification font --base --size14" href="/membros/%userID%/"> <img data-original="%userAvatar%" data-lazy="true" alt="" width="32" height="32"> <b>%userName%</b> </a> <div class="user-notifications-buttons"> <button data-type="confirm" class="js-confirm ccid_notify_ac">Aceitar</button> <button data-type="ignore" class="js-decline ccid_notify_ig">Ignorar</button> </div> </li>
      </script>
      <script id="widget_playlists_template" type="text/template">
       <li class="user-playlists-item"> <span id="js-user-menu-listen" data-endpoint="%endpoint%" data-credentials="%credentials%" data-visibility="%visibility%" class="user-playlists-play"></span> <a href="#" data-endpoint="%endpoint%" data-credentials="%credentials%" data-visibility="%visibility%"> <span>%name%</span> </a> <button class="button -edit plt_edit user-playlist-edit font --base --size12" data-hash="%hash%" data-endpoint="%endpoint%" data-credentials="%credentials%" data-visibility="%visibility%">editar</button> </li>
      </script>
      <script id="widget_songs_template" type="text/template">
       <li> <a href="/%dns%/%url%/#%hash%" class="font --base --size14"> <span class="bt-play"></span> <p>%artist% - <span>%name%</span></p> </a> </li>
      </script>
     </div>
    </div>
   </header>
   <div class="page-genre" id="all">
    <div id="cnt_top">
     <div class="--full gridContainer withRefresh an" data-refresh="20" id="pub_25" style="display:none;">
      <div id="pub_25_ad_refresh">
       <div id="pub_25_ad">
       </div>
      </div>
     </div>
     <div class="--outpage an" id="pub_6" style="display:flex;">
      <div id="pub_6_ad">
      </div>
     </div>
     <div class="homeFilter gridContainer js-genre-filter">
      <div class="filter">
       <div class="filter-tabs">
        <a class="chip --outline js-tab-link" data-genre="0" data-slug="" href="/">
         <strong class="chip-label font --base --strong --size14">
          Todos
         </strong>
        </a>
        <a class="chip --outline js-tab-link" data-genre="666" data-slug="rock" href="/estilos/rock/">
         <strong class="chip-label font --base --strong --size14">
          Rock
         </strong>
        </a>
        <a class="chip --outline js-tab-link" data-genre="30" data-slug="gospelreligioso" href="/estilos/gospelreligioso/">
         <strong class="chip-label font --base --strong --size14">
          Gospel
         </strong>
        </a>
        <a class="chip --outline js-tab-link" data-genre="9" data-slug="sertanejo" href="/estilos/sertanejo/">
         <strong class="chip-label font --base --strong --size14">
          Sertanejo
         </strong>
        </a>
        <a class="chip --outline js-tab-link" data-genre="22" data-slug="funk" href="/estilos/funk/">
         <strong class="chip-label font --base --strong --size14">
          Funk
         </strong>
        </a>
        <div class="filter-tabs-more js-cnt-filter-more-genre">
         <button class="chip --outline --dropdown isOn js-filter-more-genre" data-default="Mais" data-genre="4" data-slug="pop">
          <strong class="chip-label font --base --strong --size14">
           Pop
          </strong>
         </button>
         <div class="filter-more-dropdown modal js-cnt-filter_drop-genre" data-endpoint="/v2/genres/" data-placeholder="Digite o estilo musical">
         </div>
        </div>
       </div>
      </div>
      <a class="button --listen --topRight" data-nofollow="true" href="/estilos/pop/ouvir.html" rel="nofollow">
       Ouvir Pop ♪
      </a>
     </div>
     <div class="homeHighlight gridContainer">
      <a class="homeHighlight-link" data-ctr="hl_10167" href="https://www.letras.mus.br/lady-gaga/die-with-a-smile-feat-bruno-mars/#legenda" id="highlight">
       <img alt="" class="homeHighlight-image" height="320" src="https://akamai.sscdn.co/uploadfile/letras/imagem_destaques/10167_pt_BR_0af0425.jpg" srcset="https://akamai.sscdn.co/uploadfile/letras/imagem_destaques/10167_pt_BR_0af0425.jpg 1x, https://akamai.sscdn.co/uploadfile/letras/imagem_destaques/10167_pt_BR_0af0425_2x.jpg 2x" width="1055"/>
       <span class="button --listen">
        Ouça e confira a letra com significado dessa gigante colaboração 💙❤️
       </span>
      </a>
     </div>
     <script>
      window._hlc=[{"Name":"hlv-pt-10167","Value":"1","Expires":1724443599497}];
     </script>
     <div class="--full gridContainer withRefresh an" data-refresh="20" id="pub_4" style="display:flex;">
      <div id="pub_4_ad_refresh">
       <div id="pub_4_ad">
       </div>
      </div>
     </div>
     <div class="homeTops gridContainer">
      <a class="sectionHeader" href="/mais-acessadas/pop/">
       <h2>
        Mais acessados de Pop
       </h2>
      </a>
      <div class="homeTops-content js-cnt-target">
       <ol class="top-list_mus">
        <li>
         <a href="/lady-gaga/die-with-a-smile-feat-bruno-mars/" title="Die With A Smile (feat. Bruno Mars)">
          <b class="font --base --strong --size16">
           Die With A Smile (feat. Bruno Mars)
          </b>
          <span class="font --base --size14">
           Lady Gaga
          </span>
         </a>
        </li>
        <li>
         <a href="/billie-eilish/birds-of-a-feather/" title="BIRDS OF A FEATHER">
          <b class="font --base --strong --size16">
           BIRDS OF A FEATHER
          </b>
          <span class="font --base --size14">
           Billie Eilish
          </span>
         </a>
        </li>
        <li>
         <a href="/sandy/areia/" title="Areia (part. Lucas Lima)">
          <b class="font --base --strong --size16">
           Areia (part. Lucas Lima)
          </b>
          <span class="font --base --size14">
           Sandy
          </span>
         </a>
        </li>
        <li>
         <a href="/billie-eilish/chihiro/" title="CHIHIRO">
          <b class="font --base --strong --size16">
           CHIHIRO
          </b>
          <span class="font --base --size14">
           Billie Eilish
          </span>
         </a>
        </li>
        <li>
         <a href="/alphaville/1356/" title="Forever Young">
          <b class="font --base --strong --size16">
           Forever Young
          </b>
          <span class="font --base --size14">
           Alphaville
          </span>
         </a>
        </li>
        <li>
         <a href="/billie-eilish/wildflower/" title="WILDFLOWER">
          <b class="font --base --strong --size16">
           WILDFLOWER
          </b>
          <span class="font --base --size14">
           Billie Eilish
          </span>
         </a>
        </li>
        <li>
         <a href="/benson-boone/beautiful-things/" title="Beautiful Things">
          <b class="font --base --strong --size16">
           Beautiful Things
          </b>
          <span class="font --base --size14">
           Benson Boone
          </span>
         </a>
        </li>
        <li>
         <a href="/taylor-swift/august/" title="august">
          <b class="font --base --strong --size16">
           august
          </b>
          <span class="font --base --size14">
           Taylor Swift
          </span>
         </a>
        </li>
        <li>
         <a href="/billie-eilish/blue/" title="BLUE">
          <b class="font --base --strong --size16">
           BLUE
          </b>
          <span class="font --base --size14">
           Billie Eilish
          </span>
         </a>
        </li>
        <li>
         <a href="/ed-sheeran/photograph/" title="Photograph">
          <b class="font --base --strong --size16">
           Photograph
          </b>
          <span class="font --base --size14">
           Ed Sheeran
          </span>
         </a>
        </li>
       </ol>
       <ol class="top-list_art homeTops-content-artistList">
        <li>
         <a href="/taylor-swift/">
          <div class="thumbnail --skin-image --shape-circle --size-xLarge --tabletSize-xLarge">
           <img alt="" src="https://akamai.sscdn.co/uploadfile/letras/fotos/1/0/7/b/107bbb36057fbb04a080ee950632d372-tb5.jpg"/>
          </div>
          <b class="font --base --strong --size18">
           Taylor Swift
          </b>
         </a>
        </li>
        <li>
         <a href="/billie-eilish/">
          <div class="thumbnail --skin-image --shape-circle --size-xLarge --tabletSize-xLarge">
           <img alt="" src="https://akamai.sscdn.co/uploadfile/letras/fotos/c/3/5/3/c3536a6c436d0dd65a500dfa8b6bd7fb-tb5.jpg"/>
          </div>
          <b class="font --base --strong --size18">
           Billie Eilish
          </b>
         </a>
        </li>
        <li>
         <a href="/lady-gaga/">
          <div class="thumbnail --skin-image --shape-circle --size-xLarge --tabletSize-xLarge">
           <img alt="" src="https://akamai.sscdn.co/uploadfile/letras/fotos/e/4/a/e/e4ae6db89acab3205afd5e8a16343ef3-tb5.jpg"/>
          </div>
          <b class="font --base --strong --size18">
           Lady Gaga
          </b>
         </a>
        </li>
       </ol>
      </div>
     </div>
     <hr class="divider --large u-marginBottom40"/>
     <section class="homeBestOfThree gridContainer">
      <h2 class="sectionHeader">
       Crie playlists com seus artistas preferidos
      </h2>
      <div class="homeCreateMix gridContainer">
       <div class="homeCreateMix-suggest suggest">
        <div class="tagsInput">
         <label class="tagsInput-label" for="home-suggest-search">
          <input aria-label="Busca de artistas" autocomplete="off" class="tagsInput-input font --base --strong --size18" id="home-suggest-search" placeholder="Adicione seus artistas" type="search"/>
          <span class="tagsInput-counter font --base --strong --size14">
          </span>
          <button class="tagsInput-clearButton" title="Limpar">
           <i>
           </i>
          </button>
         </label>
        </div>
        <div class="suggest-drop modal">
         <ul class="cnt-list-check">
         </ul>
         <div class="checked-items">
         </div>
        </div>
       </div>
       <button class="homeCreateMix-submit button --listen --large font --base --strong --size18 isInactive">
        Ouvir minha playlist
       </button>
      </div>
      <h3 class="sectionHeader --small">
       Sem inspiração? Comece por aqui
      </h3>
      <div class="homeBestOfThree-items">
       <a class="homeBestOfThree-item" data-ctr="bundle_147" href="/radio.html?artists=bruno-mars,shawn-mendes,ed-sheeran">
        <img alt="" class="homeBestOfThree-item-image" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/9fd172647764b70718d76df5068cd6d1.jpg" height="191" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="191"/>
        <div class="homeBestOfThree-item-content">
         <strong class="homeBestOfThree-item-gender font --base --strong --size12">
          pop
         </strong>
         <b class="homeBestOfThree-item-artists font --base --strong --size16">
          Bruno Mars + Ed Sheeran + Shawn Mendes
         </b>
         <span class="button --listen">
          Ouvir playlist
         </span>
        </div>
       </a>
       <a class="homeBestOfThree-item" data-ctr="bundle_79" href="/radio.html?artists=taylor-swift,demi-lovato,selena-gomez">
        <img alt="" class="homeBestOfThree-item-image" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/7d0a20ccd4b2f892cf4d2299b078c880.jpg" height="191" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="191"/>
        <div class="homeBestOfThree-item-content">
         <strong class="homeBestOfThree-item-gender font --base --strong --size12">
          Pop
         </strong>
         <b class="homeBestOfThree-item-artists font --base --strong --size16">
          Taylor Swift + Selena Gomez + Demi Lovato
         </b>
         <span class="button --listen">
          Ouvir playlist
         </span>
        </div>
       </a>
       <a class="homeBestOfThree-item" data-ctr="bundle_146" href="/radio.html?artists=rammstein,ministry,stahlmann">
        <img alt="" class="homeBestOfThree-item-image" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/d9572811c2a080533af08c74c7cb5a98.jpg" height="191" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="191"/>
        <div class="homeBestOfThree-item-content">
         <strong class="homeBestOfThree-item-gender font --base --strong --size12">
          Industrial
         </strong>
         <b class="homeBestOfThree-item-artists font --base --strong --size16">
          Ministry + Rammstein + Stahlmann
         </b>
         <span class="button --listen">
          Ouvir playlist
         </span>
        </div>
       </a>
       <a class="homeBestOfThree-item" data-ctr="bundle_148" href="/radio.html?artists=ariana-grande,camila-cabello,rihanna">
        <img alt="" class="homeBestOfThree-item-image" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/da2f62f078acdbec417ed0070f189977.jpg" height="191" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="191"/>
        <div class="homeBestOfThree-item-content">
         <strong class="homeBestOfThree-item-gender font --base --strong --size12">
          pop
         </strong>
         <b class="homeBestOfThree-item-artists font --base --strong --size16">
          Rihanna + Ariana Grande + Camila Cabello
         </b>
         <span class="button --listen">
          Ouvir playlist
         </span>
        </div>
       </a>
      </div>
     </section>
     <hr class="divider --large u-marginBottom24"/>
     <div class="homePlaylists gridContainer">
      <h2 class="sectionHeader">
       <a class="sectionHeader-link" href="/playlists/todos/pop/">
        Playlists
       </a>
       <a class="button -seeMore -block" href="/playlists/todos/pop/">
        Ver mais playlists
       </a>
      </h2>
      <ul class="homePlaylistsContainer gridContainer">
       <li class="u-flex1">
        <a class="mediaList-item --playlist" data-ctr="" href="/playlists/541330/">
         <em class="mediaList-item-imageContainer">
          <div class="thumbnail --skin-image --shape-rectangle --size-proportional --tabletSize-proportional">
           <img alt="" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/5/3/1/f/531f7ee2a3234530b17ca6f00e53677d.jpg" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
          </div>
         </em>
         <div class="mediaList-item-content">
          <b class="mediaList-item-primaryText u-truncate3 font --base --size16 --mobileSize14">
           Músicas e temas de novelas
          </b>
          <span class="mediaList-item-secondaryText font --base --size14 --mobileSize12">
           Thalía, Caetano Veloso, Deborah Blando...
          </span>
         </div>
        </a>
       </li>
       <li class="u-flex1">
        <a class="mediaList-item --playlist" data-ctr="" href="/playlists/1150650/">
         <em class="mediaList-item-imageContainer">
          <div class="thumbnail --skin-image --shape-rectangle --size-proportional --tabletSize-proportional">
           <img alt="" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/f/7/5/a/f75a80230c1d47aeb137f0e50d3e99c6.jpg" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
          </div>
         </em>
         <div class="mediaList-item-content">
          <b class="mediaList-item-primaryText u-truncate3 font --base --size16 --mobileSize14">
           As melhores músicas do The Weeknd
          </b>
          <span class="mediaList-item-secondaryText font --base --size14 --mobileSize12">
           Blinding Lights, The Hills, Starboy e mais
          </span>
         </div>
        </a>
       </li>
       <li class="u-flex1">
        <a class="mediaList-item --playlist" data-ctr="" href="/playlists/952692/">
         <em class="mediaList-item-imageContainer">
          <div class="thumbnail --skin-image --shape-rectangle --size-proportional --tabletSize-proportional">
           <img alt="" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/f/e/6/6/fe66a9cca76e427bb8c8b312b2a29923.jpg" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
          </div>
         </em>
         <div class="mediaList-item-content">
          <b class="mediaList-item-primaryText u-truncate3 font --base --size16 --mobileSize14">
           As melhores músicas da Billie Eilish
          </b>
          <span class="mediaList-item-secondaryText font --base --size14 --mobileSize12">
           Happier Than Ever, lovely, bad guy...
          </span>
         </div>
        </a>
       </li>
       <li class="u-flex1">
        <a class="mediaList-item --playlist" data-ctr="" href="/playlists/934371/">
         <em class="mediaList-item-imageContainer">
          <div class="thumbnail --skin-image --shape-rectangle --size-proportional --tabletSize-proportional">
           <img alt="" data-lazy="" data-original="https://akamai.sscdn.co/uploadfile/letras/playlists/0/1/4/d/014d725490614312b2f50bbd100953c0.jpg" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
          </div>
         </em>
         <div class="mediaList-item-content">
          <b class="mediaList-item-primaryText u-truncate3 font --base --size16 --mobileSize14">
           As 30 melhores músicas da Lady Gaga
          </b>
          <span class="mediaList-item-secondaryText font --base --size14 --mobileSize12">
           Poker Face, Born This Way, Shallow...
          </span>
         </div>
        </a>
       </li>
      </ul>
     </div>
     <hr class="divider --large u-marginBottom24"/>
     <div class="homeLatestNews gridContainer dummy js-ajax-include" data-src="/latestnews.html?page=genre&amp;slug=pop">
      <h2 class="sectionHeader">
       <a class="sectionHeader-link" href="/blog/">
        Leia no Blog
       </a>
       <a class="button -seeMore" href="/blog/">
        Ver outras notícias e novidades
       </a>
      </h2>
      <div class="homeLatestNews-news">
       <div class="container homeLatestNews-new">
        <em>
         <img alt="" class="homeLatestNews-new-image" height="122" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="218"/>
        </em>
        <b>
        </b>
       </div>
       <div class="container homeLatestNews-new">
        <em>
         <img alt="" class="homeLatestNews-new-image" height="122" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="218"/>
        </em>
        <b>
        </b>
       </div>
       <div class="container homeLatestNews-new">
        <em>
         <img alt="" class="homeLatestNews-new-image" height="122" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="218"/>
        </em>
        <b>
        </b>
       </div>
       <div class="container homeLatestNews-new">
        <em>
         <img alt="" class="homeLatestNews-new-image" height="122" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="218"/>
        </em>
        <b>
        </b>
       </div>
      </div>
     </div>
     <section class="homeRecommendedSongs gridContainer dummy js-ajax-include" data-notify-parent="" data-src="/recommended_songs.ssi?page=genre&amp;genre=4">
      <h2 class="sectionHeader">
       Músicas recomendadas
      </h2>
      <div class="homeRecommendedSongs-songs">
       <div class="homeRecommendedSongs-song container">
        <img alt="" height="44" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="44"/>
        <div class="homeRecommendedSongs-info">
         <b class="homeRecommendedSongs-title font --base --strong --size16">
         </b>
         <span class="homeRecommendedSongs-artist">
         </span>
        </div>
       </div>
       <div class="homeRecommendedSongs-song container">
        <img alt="" height="44" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="44"/>
        <div class="homeRecommendedSongs-info">
         <b class="homeRecommendedSongs-title font --base --strong --size16">
         </b>
         <span class="homeRecommendedSongs-artist">
         </span>
        </div>
       </div>
       <div class="homeRecommendedSongs-song container">
        <img alt="" height="44" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="44"/>
        <div class="homeRecommendedSongs-info">
         <b class="homeRecommendedSongs-title font --base --strong --size16">
         </b>
         <span class="homeRecommendedSongs-artist">
         </span>
        </div>
       </div>
       <div class="homeRecommendedSongs-song container">
        <img alt="" height="44" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="44"/>
        <div class="homeRecommendedSongs-info">
         <b class="homeRecommendedSongs-title font --base --strong --size16">
         </b>
         <span class="homeRecommendedSongs-artist">
         </span>
        </div>
       </div>
       <div class="homeRecommendedSongs-song container">
        <img alt="" height="44" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="44"/>
        <div class="homeRecommendedSongs-info">
         <b class="homeRecommendedSongs-title font --base --strong --size16">
         </b>
         <span class="homeRecommendedSongs-artist">
         </span>
        </div>
       </div>
       <div class="homeRecommendedSongs-song container">
        <img alt="" height="44" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="44"/>
        <div class="homeRecommendedSongs-info">
         <b class="homeRecommendedSongs-title font --base --strong --size16">
         </b>
         <span class="homeRecommendedSongs-artist">
         </span>
        </div>
       </div>
      </div>
     </section>
     <section class="homeRecommendedAlbums gridContainer dummy js-ajax-include" data-src="/albums.ssi?page=genre&amp;genre=4&amp;slug=pop" data-use-cache-for-logged-off="true">
      <a class="sectionHeader" href="/top-albuns/pop/">
       <h2>
        Álbuns recomendados
       </h2>
      </a>
      <div class="homeRecommendedAlbums-albums js-cnt-target">
       <div class="mediaList-item --album">
        <em class="mediaList-item-imageContainer">
         <div class="thumbnail --skin-image --shape-square --size-proportional --tabletSize-proportional">
          <img alt="" data-lazy="" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
         </div>
        </em>
        <b>
        </b>
        <span>
        </span>
       </div>
       <div class="mediaList-item --album">
        <em class="mediaList-item-imageContainer">
         <div class="thumbnail --skin-image --shape-square --size-proportional --tabletSize-proportional">
          <img alt="" data-lazy="" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
         </div>
        </em>
        <b>
        </b>
        <span>
        </span>
       </div>
       <div class="mediaList-item --album">
        <em class="mediaList-item-imageContainer">
         <div class="thumbnail --skin-image --shape-square --size-proportional --tabletSize-proportional">
          <img alt="" data-lazy="" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
         </div>
        </em>
        <b>
        </b>
        <span>
        </span>
       </div>
       <div class="mediaList-item --album">
        <em class="mediaList-item-imageContainer">
         <div class="thumbnail --skin-image --shape-square --size-proportional --tabletSize-proportional">
          <img alt="" data-lazy="" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
         </div>
        </em>
        <b>
        </b>
        <span>
        </span>
       </div>
       <div class="mediaList-item --album">
        <em class="mediaList-item-imageContainer">
         <div class="thumbnail --skin-image --shape-square --size-proportional --tabletSize-proportional">
          <img alt="" data-lazy="" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
         </div>
        </em>
        <b>
        </b>
        <span>
        </span>
       </div>
       <div class="mediaList-item --album">
        <em class="mediaList-item-imageContainer">
         <div class="thumbnail --skin-image --shape-square --size-proportional --tabletSize-proportional">
          <img alt="" data-lazy="" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="/>
         </div>
        </em>
        <b>
        </b>
        <span>
        </span>
       </div>
      </div>
     </section>
     <div class="--full gridContainer withRefresh an" data-refresh="20" id="pub_1" style="display:flex;">
      <div id="pub_1_ad_refresh">
       <div id="pub_1_ad">
       </div>
      </div>
     </div>
     <hr class="divider --large u-marginBottom24"/>
     <section class="homeRecommendedArtists gridContainer dummy js-ajax-include" data-lazy="true" data-src="/recommended_artists.ssi?page=genre&amp;genre=4" data-threshold="300" data-use-cache-for-logged-off="true">
      <h2 class="sectionHeader">
       Artistas recomendados
      </h2>
      <ul class="homeRecommendedArtists-artists">
       <li>
        <div class="homeRecommendedArtists-artists-link">
         <img alt="" height="75" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="75"/>
         <span>
          <b class="font --base --strong --size18">
          </b>
          <small class="font --base --size14">
          </small>
         </span>
        </div>
       </li>
       <li>
        <div class="homeRecommendedArtists-artists-link">
         <img alt="" height="75" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="75"/>
         <span>
          <b class="font --base --strong --size18">
          </b>
          <small class="font --base --size14">
          </small>
         </span>
        </div>
       </li>
       <li>
        <div class="homeRecommendedArtists-artists-link">
         <img alt="" height="75" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="75"/>
         <span>
          <b class="font --base --strong --size18">
          </b>
          <small class="font --base --size14">
          </small>
         </span>
        </div>
       </li>
       <li>
        <div class="homeRecommendedArtists-artists-link">
         <img alt="" height="75" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="75"/>
         <span>
          <b class="font --base --strong --size18">
          </b>
          <small class="font --base --size14">
          </small>
         </span>
        </div>
       </li>
       <li>
        <div class="homeRecommendedArtists-artists-link">
         <img alt="" height="75" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="75"/>
         <span>
          <b class="font --base --strong --size18">
          </b>
          <small class="font --base --size14">
          </small>
         </span>
        </div>
       </li>
       <li>
        <div class="homeRecommendedArtists-artists-link">
         <img alt="" height="75" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="75"/>
         <span>
          <b class="font --base --strong --size18">
          </b>
          <small class="font --base --size14">
          </small>
         </span>
        </div>
       </li>
      </ul>
     </section>
    </div>
    <div id="cnt_footer">
     <div class="--full gridContainer with-lazy withRefresh an" data-refresh="20" id="pub_9" style="display:flex;">
      <div id="pub_9_ad_refresh">
       <div id="pub_9_ad">
       </div>
      </div>
     </div>
    </div>
   </div>
   <div class="player" id="player">
   </div>
   <div class="playerNotification font --base --size14">
   </div>
   <div class="modal contextualPlanModal" id="js-contextualPlanModal" style="transform: translate(0, 100%)">
    <h3 class="contextualPlanModal-title font --base --strong --size24 --mobileSize20">
     Navegue sem anúncios
    </h3>
    <button class="contextualPlanModal-closeButton" id="js-contextualPlanModal-close">
     Fechar
    </button>
    <p class="contextualPlanModal-subtitle font --copy --size14 contextualPlanModal-spaceBottom">
     Curta as suas músicas sem interrupções
    </p>
    <div class="contextualPlanModal-divider --withText contextualPlanModal-text contextualPlanModal-spaceBottom font --base --size12">
     <p>
      Pague uma vez e
      <strong class="font --base --strong --size12">
       use por um ano inteiro
      </strong>
     </p>
    </div>
    <div class="contextualPlanModal-cards contextualPlanModal-spaceBottom">
     <div class="contextualPlanCard --premium">
      <div class="contextualPlanCard-header">
       <i class="contextualPlanCard-header-image">
       </i>
       <p class="contextualPlanCard-header-text isLoading">
        <span class="header-text-currency font --base --strong --size10">
         R$
        </span>
        <span class="header-text-priceInteger font --base --strong --size24">
        </span>
        <span class="header-text-priceCents font --base --strong --size24">
        </span>
        <span class="header-text-period font --base --strong --size14">
         /ano
        </span>
       </p>
      </div>
      <p class="contextualPlanCard-description font --base --regular --size16">
       Use o Letras sem anúncios.
      </p>
      <div class="contextualPlanCard-button isLoading">
       <span>
       </span>
      </div>
     </div>
     <div class="contextualPlanCard --academy">
      <div class="contextualPlanCard-header">
       <i class="contextualPlanCard-header-image">
       </i>
       <div class="tag --fill --absolute --academyPrimary --xSmall">
        <span class="tag-label font --base --size12 --strong">
         Melhor escolha 🔥
        </span>
       </div>
       <p class="contextualPlanCard-header-text isLoading">
        <span class="header-text-currency font --base --strong --size10">
         R$
        </span>
        <span class="header-text-priceInteger font --base --strong --size24">
        </span>
        <span class="header-text-priceCents font --base --strong --size24">
        </span>
        <span class="header-text-period font --base --strong --size14">
         /ano
        </span>
       </p>
      </div>
      <p class="contextualPlanCard-description font --base --regular --size16">
       Benefícios Premium + aulas de idiomas com música.
      </p>
      <div class="contextualPlanCard-button isLoading">
       <span>
       </span>
      </div>
     </div>
    </div>
    <a class="button -bold contextualPlanModal-button contextualPlanModal-spaceBottom font --base --strong --size12 js-comparePlans" href="/planos.html">
     Compare os planos
    </a>
    <p class="contextualPlanModal-text font --base --size12">
     Já é assinante?
     <a class="font --base --strong --size12" href="#">
      Faça login
     </a>
     .
    </p>
   </div>
   <div class="modalOverlay">
   </div>
  </div>
  <div id="js-scripts">
   <script>
    _omq.push(['ui/genre']);
   </script>
  </div>
  <footer class="footer">
   <div class="gridContainer">
    <div class="footer-alphabet">
     <strong class="footer-label --alphabet font --base --strong --size16">
      Todos os artistas
     </strong>
     <ul class="footer-alphabet-list">
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/A/">
        A
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/B/">
        B
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/C/">
        C
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/D/">
        D
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/E/">
        E
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/F/">
        F
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/G/">
        G
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/H/">
        H
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/I/">
        I
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/J/">
        J
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/K/">
        K
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/L/">
        L
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/M/">
        M
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/N/">
        N
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/O/">
        O
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/P/">
        P
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/Q/">
        Q
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/R/">
        R
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/S/">
        S
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/T/">
        T
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/U/">
        U
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/V/">
        V
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/W/">
        W
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/X/">
        X
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/Y/">
        Y
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/Z/">
        Z
       </a>
      </li>
      <li class="footer-alphabet-item font --base --size16">
       <a href="/letra/1/">
        0/9
       </a>
      </li>
     </ul>
    </div>
    <hr class="divider --small u-marginTop24 u-marginBottom24"/>
    <div id="checkbox-bids">
    </div>
    <div class="footer-links">
     <div class="footer-nav">
      <strong class="footer-label font --base --strong --size16">
       Músicas
      </strong>
      <ul class="font --base --size14">
       <li>
        <a href="/mais-acessadas/">
         Top músicas
        </a>
       </li>
       <li>
        <a href="/novidades.html">
         Atualizações
        </a>
       </li>
       <li>
        <a href="/lancamentos.html">
         Lançamentos
        </a>
       </li>
       <li>
        <a class="no_tt" href="/playlists.html">
         Playlists do Letras
        </a>
       </li>
      </ul>
     </div>
     <div class="footer-nav">
      <strong class="footer-label font --base --strong --size16">
       Artistas
      </strong>
      <ul class="font --base --size14">
       <li>
        <a href="/mais-acessadas/">
         Top Artistas
        </a>
       </li>
       <li>
        <a href="/top-albuns/">
         Top Álbuns
        </a>
       </li>
      </ul>
     </div>
     <div class="footer-nav">
      <strong class="footer-label font --base --strong --size16">
       Participe
      </strong>
      <ul class="font --base --size14">
       <li>
        <a href="/perfil_musical.html">
         Crie seu perfil musical
        </a>
       </li>
       <li>
        <a data-ct-action="Nav Enviar Album" data-ct-label="Link (rodape)" href="/contribuicoes/" rel="nofollow">
         Envie álbuns
        </a>
       </li>
       <li>
        <a data-ct-action="Nav Enviar Letras" data-ct-label="Link (rodape)" href="/contribuicoes/" rel="nofollow">
         Envie letras
        </a>
       </li>
       <li>
        <a data-ct-action="Nav Enviar Correcao" data-ct-label="Link (rodape)" href="/contribuicoes/" rel="nofollow">
         Correções de letras
        </a>
       </li>
       <li>
        <a data-ct-action="Nav Assine o Letras" data-ct-label="Link (rodape)" href="/planos.html?utm_source=letras.mus.br&amp;utm_medium=footer&amp;utm_id=footer&amp;utm_campaign=assine" rel="nofollow">
         Assine o Letras
        </a>
       </li>
      </ul>
     </div>
     <div class="footer-nav">
      <strong class="footer-label font --base --strong --size16">
       Sobre o site
      </strong>
      <ul class="font --base --size14" id="legal-links">
       <li>
        <a href="/faq.html">
         Ajuda
        </a>
       </li>
       <li>
        <a href="/aviso-legal.html">
         Termos de uso e Política de privacidade
        </a>
       </li>
       <li>
        <a href="/aviso-legal-academy.html">
         Termos de uso do Letras Academy
        </a>
       </li>
       <li id="change-consent" style="display:none;">
        <a href="#change-consent" onclick="window.__tcfapi('displayConsentUi', 2, function() {} );">
         Configurações de privacidade
        </a>
       </li>
       <li>
        <a href="/padroes-para-envios.html">
         Padrões para envios
        </a>
       </li>
       <li>
        <a href="/trabalheconosco">
         Trabalhe Conosco
        </a>
       </li>
      </ul>
     </div>
    </div>
    <hr class="divider --small u-marginTop24 u-marginBottom24"/>
    <div class="footer-apps">
     <div>
      <strong class="footer-label font --base --strong --size16">
       Aplicativos
      </strong>
      <div class="footer-apps-list">
       <a aria-label="Google Play Store" class="footer-apps-store --googlePlay" href="https://play.google.com/store/apps/details?id=com.studiosol.player.letras&amp;hl=pt" rel="noopener" target="_blank">
        <i>
        </i>
       </a>
       <a aria-label="App Store" class="footer-apps-store --appStore" href="https://itunes.apple.com/pt/app/letras.mus.br/id773347891?mt=8" rel="noopener" target="_blank">
        <i>
        </i>
       </a>
      </div>
     </div>
     <div>
      <div class="footer-apps-extension">
       <strong class="footer-label font --base --strong --size16">
        Extensão
       </strong>
       <div class="footer-apps-list">
        <a aria-label="Extensão para Google Chrome" class="footer-apps-chrome" href="/plugin/chrome/">
         <i>
         </i>
        </a>
       </div>
      </div>
      <div>
       <strong class="footer-label font --base --strong --size16">
        Localização e idioma
       </strong>
       <div class="footer-locale">
        <div>
         <button class="js-select footer-select footer-locale-select font --base --size14" data-menu="region">
          Brasil
         </button>
         <div class="js-selectOptions footer-selectOptions" data-menu="region">
          <button data-value="ar">
           Argentina
          </button>
          <button class="isSelected" data-value="pt">
           Brasil
          </button>
          <button data-value="co">
           Colômbia
          </button>
          <button data-value="sp">
           Espanha
          </button>
          <button data-value="es">
           Hispanoamérica
          </button>
          <button data-value="mx">
           México
          </button>
         </div>
        </div>
        <div>
         <button class="js-select footer-select footer-locale-select font --base --size14" data-menu="language">
          Português
         </button>
         <div class="js-selectOptions footer-selectOptions" data-menu="language">
          <button class="isSelected" data-value="pt_BR">
           Português
          </button>
          <button data-value="en_US">
           English
          </button>
          <button data-value="es_ES">
           Español
          </button>
         </div>
        </div>
       </div>
      </div>
     </div>
     <div class="footer-theme">
      <strong class="footer-label font --base --strong --size16">
       Tema
      </strong>
      <div>
       <button class="js-select footer-select footer-theme-select font --base --size14" data-menu="theme">
        Automático
       </button>
       <div class="js-selectOptions footer-selectOptions" data-menu="theme">
        <button data-value="auto">
         Automático
        </button>
        <button data-value="light">
         Claro
        </button>
        <button data-value="dark">
         Escuro
        </button>
       </div>
      </div>
     </div>
    </div>
    <hr class="divider --small u-marginTop24 u-marginBottom24"/>
    <div class="footer-social g-fix">
     <strong class="footer-label font --base --strong --size16">
      Siga o Letras
     </strong>
     <div class="footer-follows">
      <a class="footer-follow --instagram font --base --strong --size14" href="https://www.instagram.com/letrasmusbr/" rel="noopener" target="_blank">
       <i>
       </i>
       <span>
        Instagram
       </span>
      </a>
      <a class="footer-follow --tiktok font --base --strong --size14" href="https://www.tiktok.com/@letras" rel="noopener" target="_blank">
       <i>
       </i>
       <span>
        TikTok
       </span>
      </a>
      <a class="footer-follow --youtube font --base --strong --size14" href="https://www.youtube.com/letrasmusbr" rel="noopener" target="_blank">
       <i>
       </i>
       <span>
        YouTube
       </span>
      </a>
      <a class="footer-follow --facebook font --base --strong --size14" href="https://facebook.com/letrasmusbr" rel="noopener" target="_blank">
       <i>
       </i>
       <span>
        Facebook
       </span>
      </a>
      <a class="footer-follow --x font --base --strong --size14" href="https://x.com/letras" rel="noopener" target="_blank">
       <i>
       </i>
       <span>
        X
       </span>
      </a>
      <a class="footer-follow --pinterest font --base --strong --size14" href="https://br.pinterest.com/letrasmusbr" rel="noopener" target="_blank">
       <i>
       </i>
       <span>
        Pinterest
       </span>
      </a>
      <a class="footer-follow --linkedin font --base --strong --size14" href="https://www.linkedin.com/company/letras/" rel="noopener" target="_blank">
       <i>
       </i>
       <span>
        Linkedin
       </span>
      </a>
     </div>
    </div>
    <hr class="divider --small u-marginTop24 u-marginBottom24"/>
    <div class="footer-external">
     <div class="footer-external-item">
      <p class="footer-external-label">
       Conheça também:
      </p>
      <div class="footer-external-links">
       <a class="footer-external-link --academy" href="/academy/">
        Letras Academy
       </a>
      </div>
     </div>
     <div class="footer-external-item">
      <p class="footer-external-label">
       Baixe o Letras Academy:
      </p>
      <div class="footer-external-links">
       <a aria-label="App Store" class="footer-external-link --appStore" href="https://itunes.apple.com/br/app/letras-academy/id1603626307?mt=8" rel="noopener" target="_blank">
       </a>
      </div>
     </div>
     <div class="footer-external-item">
      <p class="footer-external-label">
       Mais música em:
      </p>
      <div class="footer-external-links">
       <a class="footer-external-link --cifraClub" href="https://www.cifraclub.com.br/">
        Cifra Club
       </a>
       <a class="footer-external-link --palco" href="https://www.palcomp3.com/">
        Palco MP3
       </a>
       <a class="footer-external-link --lyricslayers" href="https://www.lyricslayers.com/">
        Lyrics Layers
       </a>
      </div>
     </div>
    </div>
    <p class="footer-letrasText font --copy --size14">
     <span>
      Música começa com letras
     </span>
     <span>
      © 2003 - 2024, 3.4 milhões de letras de músicas, 53.3 milhões de visitas em Julho
     </span>
     <span>
      Feito com
      <b class="footer-letrasText-heart">
       amor
      </b>
      em Belo Horizonte
     </span>
    </p>
    <div class="footer-images">
     <i class="footer-image --museum" title="Museu de Artes e Ofícios">
     </i>
     <i class="footer-image --church" title="Igreja de São Francisco de Assis">
     </i>
     <i class="footer-image --square" title="Obelisco da Praça Sete de Setembro">
     </i>
    </div>
   </div>
   <div id="js-footer-cmp">
   </div>
  </footer>
  <div class="modal editPlaylist" id="edit-playlist">
   <div class="editPlaylist-content">
    <h2 class="sectionHeader">
     Editar playlist
    </h2>
    <div class="editPlaylist-confirmation --delete">
     <span>
      Tem certeza que deseja excluir esta playlist?
     </span>
     <button class="editPlaylist-deleteCancel">
      Cancelar
     </button>
     <button class="editPlaylist-deleteConfirm">
      Excluir
     </button>
    </div>
    <div class="editPlaylist-confirmation --close">
     <span>
      Tem certeza que deseja sair sem salvar suas alterações?
     </span>
     <button class="editPlaylist-closeCancel">
      Cancelar
     </button>
     <button class="editPlaylist-closeConfirm">
      Sair sem salvar
     </button>
    </div>
    <div class="editPlaylist-actions">
     <button class="editPlaylist-deleteButton font --base --size12">
      Excluir playlist
     </button>
     <button class="button -bold editPlaylist-cancel">
      Cancelar
     </button>
     <button class="button -violet editPlaylist-save">
      Salvar
     </button>
    </div>
    <form class="editPlaylist-form">
     <div class="editPlaylist-name">
      <label class="label">
       Nome
      </label>
      <input class="input editPlaylist-name-input" value=""/>
      <span class="editPlaylist-name-counter font --base --strong --size12">
      </span>
     </div>
     <div class="editPlaylist-visibility">
      <label class="label">
       Quem pode ouvir
      </label>
      <div>
       <label class="editPlaylist-visibility-check font --base --size16">
        <input checked="" class="radioButton-component --medium" name="visibility" type="radio" value="public"/>
        <span>
         Todos
        </span>
       </label>
       <label class="editPlaylist-visibility-check font --base --size16">
        <input checked="" class="radioButton-component --medium" name="visibility" type="radio" value="me"/>
        <span>
         Somente eu
        </span>
       </label>
      </div>
     </div>
     <hr class="divider --large u-marginBottom20 editPlaylist-line"/>
     <div>
      <label class="label">
       Adicionar músicas
      </label>
      <div class="suggest">
       <input autocomplete="off" class="s_input input" id="edit-playlist_suggest" placeholder="Que música deseja adicionar?"/>
       <div class="suggest-drop modal">
        <ul class="cnt-list-check">
        </ul>
       </div>
      </div>
     </div>
    </form>
    <div class="editPlaylist-results ps">
     <ul class="cnt-list sortable">
     </ul>
    </div>
   </div>
  </div>
  <div class="modalOverlay js-edit-playlist-overlay">
  </div>
  <script id="edit_playlist_list_item" type="text/template">
   <li data-lid="%id%" data-id="%playlistSongID%"> <span class="editPlaylist-selectOrder"> <select class="editPlaylist-selectOrder-select font --base --size16"></select> </span> <a href="#" data-nofollow="true"><b>%artist%</b> - %name%</a> <i class="x" title='remover'></i> </li>
  </script>
  <script id="modal_item_suggest" type="text/template">
   <li data-lid="%imu%" data-dns="%dns%" data-url="%url%" data-name="%txt%%extra_txt%" data-art="%art%"> <a href="#">%art% - %txt%%extra_txt%</a> </li>
  </script>
  <script>
   if (!("IntersectionObserver" in window)) {
                var s = document.createElement("script");
                s.async = false;
                s.src = '//akamai.sscdn.co/letras/desktop/static/js/polyfills-pt.v12d3255c.js';
                document.head.appendChild(s);
        }
  </script>
  <script async="" src="https://akamai.sscdn.co/gcs/letras-static/ads/js/hb_letras.ff6789a56930e5b63342.m.js" type="module">
  </script>
  <script async="" nomodule="" src="https://akamai.sscdn.co/gcs/letras-static/ads/js/hb_letras.0712bbf94abc31899164.js">
  </script>
  <script async="" src="https://akamai.sscdn.co/gcs/letras-static/ads/js/prebid_all.5487a3e0fa95e7b85d34285d6e5d9208.js">
  </script>
  <script async="" crossorigin="anonymous" src="https://securepubads.g.doubleclick.net/tag/js/gpt.js">
  </script>
  <script async="" src="https://c.amazon-adsystem.com/aax2/apstag.js">
  </script>
  <script async="" src="//akamai.sscdn.co/letras/desktop/static/js/index.m-pt.v83108c76.js" type="module">
  </script>
  <script async="" nomodule="" src="//akamai.sscdn.co/letras/desktop/static/js/index-pt.v4130a378.js">
  </script>
  <script>
   (function (w, d, s, l, i) {
    w[l] = w[l] || []; w[l].push({
        'gtm.start':
            new Date().getTime(), event: 'gtm.js'
    }); var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
            'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
})(window, document, 'script', 'dataLayer', 'GTM-KWMSHG8');
window.dataLayer = window.dataLayer || [];
  </script>
  <noscript>
   <iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-KWMSHG8" style="display:none;visibility:hidden" width="0">
   </iframe>
  </noscript>
 </body>
'''