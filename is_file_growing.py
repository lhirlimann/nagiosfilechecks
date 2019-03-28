






<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-7uoDIEGQ8zTwUS9KjTP+/2I13FQPHvJ9EKoeUThfin5R1+27bcUC08VQzUo4CIjCdhvJM4zxuI+3HcSycAUTCg==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-abba74d6e28a6842788159fec056bf26.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-P8Cxw38V/FRYDTa1W9y3m4RSDpiLCSutzqj1FwwRHI0S6u+SwjonMes9E6PE9j7NLPaj55u/5Fz86JS7MR7Kmw==" rel="stylesheet" href="https://github.githubassets.com/assets/github-c2ffc17b6aaa94556eada69593801635.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>is_file_growing.py</title>
    <meta name="description" content="GitHub Gist: instantly share code, notes, and snippets.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch-gist.xml" title="Gist">
  <link rel="fluid-icon" href="https://gist.github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars3.githubusercontent.com/u/65812?s=400&amp;v=4" /><meta property="og:site_name" content="Gist" /><meta property="og:type" content="article" /><meta property="og:title" content="is_file_growing.py" /><meta property="og:url" content="https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808" /><meta property="og:description" content="GitHub Gist: instantly share code, notes, and snippets." /><meta property="article:author" content="262588213843476" /><meta property="article:publisher" content="262588213843476" />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MzYxOTc2NDgyOjU5ZjJmOTRjODgyZjE3YjU1NmQ0NWIxYWNmODk5OTVkMTQ5MDBjYTBkMDM1NzA3MzIyYjhkY2U1MDBlZWJhZGI=--6aa4b29546fbb746800350b3886a8fb86f673830">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="D408:62D1:4AB15A:82C4F4:5C9C9849" data-pjax-transient>


  

  <meta name="selected-link" value="gist_code" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="gist" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="D408:62D1:4AB15A:82C4F4:5C9C9849" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="415751" /><meta name="octolytics-actor-login" content="lhirlimann" /><meta name="octolytics-actor-hash" content="722f260c938e00a0d8ec796ce95505bb5de0b12247465d327f9eb54f9cc81253" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;gist-id&gt;" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-4">

  <meta class="js-ga-set" name="userId" content="0dd71c37e5a50511889dd9bcfc8f5ae7">

<meta class="js-ga-set" name="dimension1" content="Logged In">



    <meta name="octolytics-dimension-public" content="true" /><meta name="octolytics-dimension-gist_id" content="16582398" /><meta name="octolytics-dimension-gist_name" content="37337b8dc70ca4da9808" /><meta name="octolytics-dimension-anonymous" content="false" /><meta name="octolytics-dimension-owner_id" content="65812" /><meta name="octolytics-dimension-owner_login" content="JustinAzoff" /><meta name="octolytics-dimension-forked" content="false" />

  <meta class="js-ga-set" name="dimension5" content="public">
  <meta class="js-ga-set" name="dimension6" content="owned">
  <meta class="js-ga-set" name="dimension7" content="python">


      <meta name="hostname" content="gist.github.com">
    <meta name="user-login" content="lhirlimann">

      <meta name="expected-hostname" content="gist.github.com">
    <meta name="js-proxy-site-detection-payload" content="N2Q1OWU4OTVmNmZiN2NhNzQ0MDZlNTY0MjdiN2ZmNThjZTQ2NzdlMjM5NzNkMzQ2OTgzMjk0YjcyZDI0N2IxNnx7InJlbW90ZV9hZGRyZXNzIjoiNzguMjEyLjg4LjE2NyIsInJlcXVlc3RfaWQiOiJENDA4OjYyRDE6NEFCMTVBOjgyQzRGNDo1QzlDOTg0OSIsInRpbWVzdGFtcCI6MTU1Mzc2NjQ3MywiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="UNIVERSE_BANNER,MARKETPLACE_SOCIAL_PROOF,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_UNVERIFIED_LISTINGS,MARKETPLACE_PLAN_RESTRICTION_EDITOR,NOTIFY_ON_BLOCK,RELATED_ISSUES">

  <meta name="html-safe-nonce" content="165367adf43fd976c792f8fccfa7b6b36f7208fe">

  <meta http-equiv="x-pjax-version" content="fcbe73790c3849ab79f0456dd8333fe5">
  

      <link href="/JustinAzoff.atom" rel="alternate" title="atom" type="application/atom+xml">

  <link crossorigin="anonymous" media="all" integrity="sha512-ePMbNH3eB0y5p/LoLTm3+eI53PhyUA2g0PwJs8nLZjVeVo3BK19Hj3cr8Fyuc9L9ZhbHSw85qEXrHM/63nUYOQ==" rel="stylesheet" href="https://github.githubassets.com/assets/gist-6ab0fc42583fec2f0a334dce30e3b3cc.css" />




  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">





  </head>

  <body class="logged-in env-production">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        <div class="Header-old gist-header header-logged-in" role="banner">
  <div class="container-lg px-3 clearfix">
    <div class="d-flex flex-justify-between">
      <div class="d-flex">
        <a class="header-logo-wordmark" data-hotkey="g d" aria-label="Gist Homepage" href="/">
          <svg width="78" height="28" class="octicon octicon-logo-github" viewBox="0 0 45 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M18.53 12.03h-.02c.009 0 .015.01.024.011h.006l-.01-.01zm.004.011c-.093.001-.327.05-.574.05-.78 0-1.05-.36-1.05-.83V8.13h1.59c.09 0 .16-.08.16-.19v-1.7c0-.09-.08-.17-.16-.17h-1.59V3.96c0-.08-.05-.13-.14-.13h-2.16c-.09 0-.14.05-.14.13v2.17s-1.09.27-1.16.28c-.08.02-.13.09-.13.17v1.36c0 .11.08.19.17.19h1.11v3.28c0 2.44 1.7 2.69 2.86 2.69.53 0 1.17-.17 1.27-.22.06-.02.09-.09.09-.16v-1.5a.177.177 0 0 0-.146-.18zM42.23 9.84c0-1.81-.73-2.05-1.5-1.97-.6.04-1.08.34-1.08.34v3.52s.49.34 1.22.36c1.03.03 1.36-.34 1.36-2.25zm2.43-.16c0 3.43-1.11 4.41-3.05 4.41-1.64 0-2.52-.83-2.52-.83s-.04.46-.09.52c-.03.06-.08.08-.14.08h-1.48c-.1 0-.19-.08-.19-.17l.02-11.11c0-.09.08-.17.17-.17h2.13c.09 0 .17.08.17.17v3.77s.82-.53 2.02-.53l-.01-.02c1.2 0 2.97.45 2.97 3.88zm-8.72-3.61h-2.1c-.11 0-.17.08-.17.19v5.44s-.55.39-1.3.39-.97-.34-.97-1.09V6.25c0-.09-.08-.17-.17-.17h-2.14c-.09 0-.17.08-.17.17v5.11c0 2.2 1.23 2.75 2.92 2.75 1.39 0 2.52-.77 2.52-.77s.05.39.08.45c.02.05.09.09.16.09h1.34c.11 0 .17-.08.17-.17l.02-7.47c0-.09-.08-.17-.19-.17zm-23.7-.01h-2.13c-.09 0-.17.09-.17.2v7.34c0 .2.13.27.3.27h1.92c.2 0 .25-.09.25-.27V6.23c0-.09-.08-.17-.17-.17zm-1.05-3.38c-.77 0-1.38.61-1.38 1.38 0 .77.61 1.38 1.38 1.38.75 0 1.36-.61 1.36-1.38 0-.77-.61-1.38-1.36-1.38zm16.49-.25h-2.11c-.09 0-.17.08-.17.17v4.09h-3.31V2.6c0-.09-.08-.17-.17-.17h-2.13c-.09 0-.17.08-.17.17v11.11c0 .09.09.17.17.17h2.13c.09 0 .17-.08.17-.17V8.96h3.31l-.02 4.75c0 .09.08.17.17.17h2.13c.09 0 .17-.08.17-.17V2.6c0-.09-.08-.17-.17-.17zM8.81 7.35v5.74c0 .04-.01.11-.06.13 0 0-1.25.89-3.31.89-2.49 0-5.44-.78-5.44-5.92S2.58 1.99 5.1 2c2.18 0 3.06.49 3.2.58.04.05.06.09.06.14L7.94 4.5c0 .09-.09.2-.2.17-.36-.11-.9-.33-2.17-.33-1.47 0-3.05.42-3.05 3.73s1.5 3.7 2.58 3.7c.92 0 1.25-.11 1.25-.11v-2.3H4.88c-.11 0-.19-.08-.19-.17V7.35c0-.09.08-.17.19-.17h3.74c.11 0 .19.08.19.17z"/></svg>
          <svg width="40" height="28" class="octicon octicon-logo-gist" viewBox="0 0 25 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M4.7 8.73h2.45v4.02c-.55.27-1.64.34-2.53.34-2.56 0-3.47-2.2-3.47-5.05 0-2.85.91-5.06 3.48-5.06 1.28 0 2.06.23 3.28.73V2.66C7.27 2.33 6.25 2 4.63 2 1.13 2 0 4.69 0 8.03c0 3.34 1.11 6.03 4.63 6.03 1.64 0 2.81-.27 3.59-.64V7.73H4.7v1zm6.39 3.72V6.06h-1.05v6.28c0 1.25.58 1.72 1.72 1.72v-.89c-.48 0-.67-.16-.67-.7v-.02zm.25-8.72c0-.44-.33-.78-.78-.78s-.77.34-.77.78.33.78.77.78.78-.34.78-.78zm4.34 5.69c-1.5-.13-1.78-.48-1.78-1.17 0-.77.33-1.34 1.88-1.34 1.05 0 1.66.16 2.27.36v-.94c-.69-.3-1.52-.39-2.25-.39-2.2 0-2.92 1.2-2.92 2.31 0 1.08.47 1.88 2.73 2.08 1.55.13 1.77.63 1.77 1.34 0 .73-.44 1.42-2.06 1.42-1.11 0-1.86-.19-2.33-.36v.94c.5.2 1.58.39 2.33.39 2.38 0 3.14-1.2 3.14-2.41 0-1.28-.53-2.03-2.75-2.23h-.03zm8.58-2.47v-.86h-2.42v-2.5l-1.08.31v2.11l-1.56.44v.48h1.56v5c0 1.53 1.19 2.13 2.5 2.13.19 0 .52-.02.69-.05v-.89c-.19.03-.41.03-.61.03-.97 0-1.5-.39-1.5-1.34V6.94h2.42v.02-.01z"/></svg>
</a>
        <div class="site-search js-site-search">
            <div class="header-search">

<!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative js-quicksearch-form" role="search" aria-label="Site" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <div class="header-search-wrapper form-control js-chromeless-input-container">
    <input type="text"
      class="form-control js-site-search-focus header-search-input js-navigation-enable js-quicksearch-field"
      data-hotkey="s,/"
      name="q"
      aria-label="Search"
      placeholder="Search…"
      autocorrect="off"
      autocomplete="off"
      autocapitalize="off">
  </div>

    <div class="gist-quicksearch-results js-quicksearch-results js-navigation-container" data-quicksearch-url="/search/quick"></div>
</form></div>

        </div>

        <nav aria-label="Global" class="d-flex">
          <ul class="list-style-none d-flex flex-items-center text-bold pl-2">
            <li><a class="HeaderNavlink px-2" data-ga-click="Header, go to all gists, text:all gists" href="/discover">All gists</a></li>
            <li><a class="HeaderNavlink px-2" data-ga-click="Header, go to GitHub, text:Back to GitHub" href="https://github.com">Back to GitHub</a></li>
          </ul>
        </nav>
      </div>

        <ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
          <li><a class="HeaderNavlink text-bold pr-3" data-ga-click="Header, go to new gist, text:new gist" href="/">New gist</a></li>
          <li class="dropdown">
            <details class="details-overlay details-reset pl-2">
              <summary class="HeaderNavlink name mt-1"
                aria-label="View profile and more"
                data-ga-click="Header, show menu, icon:avatar">
                <img class="avatar" src="https://avatars2.githubusercontent.com/u/415751?s=40&amp;v=4" width="20" height="20" alt="@lhirlimann" />
                <span class="dropdown-caret"></span>
              </summary>
              <details-menu class="dropdown-menu dropdown-menu-sw">
                <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/lhirlimann" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">lhirlimann</strong></a></div>
                <div role="none" class="dropdown-divider"></div>
                <a role="menuitem" class="dropdown-item" href="/lhirlimann" data-ga-click="Header, go to your gists, text:your gists">Your gists</a>
                <a role="menuitem" class="dropdown-item" href="/lhirlimann/starred" data-ga-click="Header, go to starred gists, text:starred gists">Starred gists</a>
                <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
                <div role="none" class="dropdown-divider"></div>
                <a role="menuitem" class="dropdown-item" href="https://github.com/lhirlimann" data-ga-click="Header, go to profile, text:your profile">Your GitHub profile</a>
                <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="https://gist.github.com/auth/github/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="/mFwA2bbLZDNXBEZXBjn4sumIidACp980+qq+ji6mflHW4ng89rdNK/lS3A8dJUyf3wd5kgE3qLByPfbJsftCw==" />
                  <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
                    Sign out
                  </button>
</form>              </details-menu>
            </details>
          </li>
        </ul>
    </div>
  </div>
</div>



      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/Code">
    <main id="gist-pjax-container" class="gist-content-wrapper" data-pjax-container>
      




<div class="gisthead pagehead repohead instapaper_ignore readability-menu experiment-repo-nav mb-4">
  <div class="container-lg px-3">
    
  
<div class="mb-3 d-flex">

  <h1 class="public css-truncate float-none flex-auto width-fit pl-0">
    <a class="avatar mr-1" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=65812" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/JustinAzoff"><img src="https://avatars2.githubusercontent.com/u/65812?s=52&amp;v=4" width="26" height="26" alt="@JustinAzoff" /></a>
    <span class="author"><a data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=65812" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/JustinAzoff">JustinAzoff</a></span><!--
        --><span class="path-divider">/</span><!--
        --><strong itemprop="name" class="gist-header-title css-truncate-target"><a href="/JustinAzoff/37337b8dc70ca4da9808">is_file_growing.py</a></strong>

    <div class="d-block text-small text-gray">
      Last active <time-ago datetime="2015-08-29T14:10:23Z">Aug 29, 2015</time-ago>
        &bull;
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" method="post" action="/JustinAzoff/37337b8dc70ca4da9808/report"><input class="btn-link link-gray" aria-label="Report gist as abuse" data-confirm="Do you want to report the contents of this gist as abuse?" type="submit" value="Report abuse" /><input type="hidden" name="authenticity_token" value="o99vDIVaXs2Qb64E7reyThEwCV4U+bgQ4MRC/2VMTMPN4Ix+SZZoC/FHrWMUWbD/KqIJV5qfC23mZdi4e5V5Fw==" /></form>
    </div>
  </h1>

  <ul class="pagehead-actions float-none">


    <li>
          <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/JustinAzoff/37337b8dc70ca4da9808/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="ClF+AXozu4B9SRaXxb+agcoiyuszxvWtlV5ZBSX9v3WmjIkcm/tL+OfBzEn19oQ1qZM2hzDJqSPUuCnSbYGyNw==" />
      <input type="hidden" name="context" value="gist"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this gist" title="Unstar JustinAzoff/37337b8dc70ca4da9808" data-ga-click="Repository, click unstar button, action:gists/gists#show; text:Unstar">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
</button>        <a class="social-count js-social-count" href="/JustinAzoff/37337b8dc70ca4da9808/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/JustinAzoff/37337b8dc70ca4da9808/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="PKcT3WmwF8k/DPKs7vqPJCQbsm1L4C7sr+xm8mqVEt4TzQ9QID0QkevXz3YU0F+PKKcjdDKDTA/9UXLKeuGOYQ==" />
      <input type="hidden" name="context" value="gist"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this gist" title="Star JustinAzoff/37337b8dc70ca4da9808" data-ga-click="Repository, click star button, action:gists/gists#show; text:Star">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
</button>        <a class="social-count js-social-count" href="/JustinAzoff/37337b8dc70ca4da9808/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>


    </li>

      <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/JustinAzoff/37337b8dc70ca4da9808/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="EIXvmr7IAxlMY4d7ry9IVMwxQIu84SJLpySC6xdQ6Y+jriYHpfinakCIZt+1/gZ2rBdKAdEJib0UkrLk5K6DVQ==" />
    <button class="btn btn-sm btn-with-count" type="submit">
      <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      Fork
    </button>
      <span class="social-count">0</span>
</form>
      </li>
  </ul>

</div>

<div class="d-flex">
  <div class="flex-auto">
    <nav class="reponav js-repo-nav js-sidenav-container-pjax"
     aria-label="Gist"
     data-pjax="#gist-pjax-container">

  <a class="js-selected-navigation-item selected reponav-item" aria-label="Code" data-pjax="true" data-hotkey="g c" aria-current="page" data-selected-links="gist_code /JustinAzoff/37337b8dc70ca4da9808" href="/JustinAzoff/37337b8dc70ca4da9808">
    <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
    Code
</a>
    <a class="js-selected-navigation-item reponav-item" aria-label="Revisions" data-pjax="true" data-hotkey="g r" data-selected-links="gist_revisions /JustinAzoff/37337b8dc70ca4da9808/revisions" href="/JustinAzoff/37337b8dc70ca4da9808/revisions">
      <svg class="octicon octicon-git-commit" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"/></svg>
      Revisions
      <span class="Counter">2</span>
</a>

</nav>

  </div>

  <div class="file-navigation-options" data-multiple>

    <div class="file-navigation-option v-align-middle">

  <div class="input-group js-gist-share-menu">
    <div class="input-group-button">
      <details class="details-reset details-overlay select-menu">
        <summary class="btn btn-sm select-menu-button" data-ga-click="Repository, clone Embed, location:repo overview">
          <span data-menu-button>Embed</span>
        </summary>
        <details-menu class="select-menu-modal position-absolute" style="z-index: 99;" aria-label="Clone options">
          <div class="select-menu-header">
            <span class="select-menu-title">What would you like to do?</span>
          </div>
          <div class="select-menu-list">
              <button name="button" type="button" class="select-menu-item width-full" aria-checked="true" role="menuitemradio" tabindex="0" value="&lt;script src=&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808.js&quot;&gt;&lt;/script&gt;" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;EMBED&quot;,&quot;git_repository_type&quot;:&quot;GIST&quot;,&quot;gist_id&quot;:16582398,&quot;client_id&quot;:&quot;1682679581.1547210180&quot;,&quot;originating_request_id&quot;:&quot;D408:62D1:4AB15A:82C4F4:5C9C9849&quot;,&quot;originating_url&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;referrer&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;user_id&quot;:415751}}" data-hydro-click-hmac="f7400b1df9c5d0b9a48eecaa2b04bcba6a03f1a08a749c7b4272eac97ad0a711">
                <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                <div class="select-menu-item-text">
                  <span class="select-menu-item-heading" data-menu-button-text>
                    
                    Embed
                  </span>
                    <span class="description">
                      Embed this gist in your website.
                    </span>
                </div>
</button>              <button name="button" type="button" class="select-menu-item width-full" aria-checked="false" role="menuitemradio" tabindex="0" value="https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;SHARE&quot;,&quot;git_repository_type&quot;:&quot;GIST&quot;,&quot;gist_id&quot;:16582398,&quot;client_id&quot;:&quot;1682679581.1547210180&quot;,&quot;originating_request_id&quot;:&quot;D408:62D1:4AB15A:82C4F4:5C9C9849&quot;,&quot;originating_url&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;referrer&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;user_id&quot;:415751}}" data-hydro-click-hmac="bee6c755a090674dce82979e62efddfe1c6890fc0691aadd9dc305f7dd09652c">
                <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                <div class="select-menu-item-text">
                  <span class="select-menu-item-heading" data-menu-button-text>
                    
                    Share
                  </span>
                    <span class="description">
                      Copy sharable link for this gist.
                    </span>
                </div>
</button>              <button name="button" type="button" class="select-menu-item width-full" aria-checked="false" role="menuitemradio" tabindex="0" value="https://gist.github.com/37337b8dc70ca4da9808.git" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_HTTPS&quot;,&quot;git_repository_type&quot;:&quot;GIST&quot;,&quot;gist_id&quot;:16582398,&quot;client_id&quot;:&quot;1682679581.1547210180&quot;,&quot;originating_request_id&quot;:&quot;D408:62D1:4AB15A:82C4F4:5C9C9849&quot;,&quot;originating_url&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;referrer&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;user_id&quot;:415751}}" data-hydro-click-hmac="656b8c4fff8009b3a5ec64de82f6e9ed2d434f9ac3291b921f4493ede6a5d8ac">
                <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                <div class="select-menu-item-text">
                  <span class="select-menu-item-heading" data-menu-button-text>
                    Clone via
                    HTTPS
                  </span>
                    <span class="description">
                      Clone with Git or checkout with SVN using the repository’s web address.
                    </span>
                </div>
</button>              <button name="button" type="button" class="select-menu-item width-full" aria-checked="false" role="menuitemradio" tabindex="0" value="git@gist.github.com:37337b8dc70ca4da9808.git" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_SSH&quot;,&quot;git_repository_type&quot;:&quot;GIST&quot;,&quot;gist_id&quot;:16582398,&quot;client_id&quot;:&quot;1682679581.1547210180&quot;,&quot;originating_request_id&quot;:&quot;D408:62D1:4AB15A:82C4F4:5C9C9849&quot;,&quot;originating_url&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;referrer&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;user_id&quot;:415751}}" data-hydro-click-hmac="ee1189459ab6302e825f017af31b8b8b6153cfd4fb1abf66c10ba8b777d690f6">
                <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                <div class="select-menu-item-text">
                  <span class="select-menu-item-heading" data-menu-button-text>
                    Clone via
                    SSH
                  </span>
                    <span class="description">
                      Clone with an SSH key and passphrase from your GitHub settings.
                    </span>
                </div>
</button>          </div>
          <div class="select-menu-list" role="menu">
            <a class="select-menu-item select-menu-action" href="https://help.github.com/articles/which-remote-url-should-i-use" target="_blank">
              <svg class="octicon octicon-question select-menu-item-icon" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6 10h2v2H6v-2zm4-3.5C10 8.64 8 9 8 9H6c0-.55.45-1 1-1h.5c.28 0 .5-.22.5-.5v-1c0-.28-.22-.5-.5-.5h-1c-.28 0-.5.22-.5.5V7H4c0-1.5 1.5-3 3-3s3 1 3 2.5zM7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7z"/></svg>
              <div class="select-menu-item-text">
                Learn more about clone URLs
              </div>
            </a>
          </div>
        </details-menu>
      </details>
    </div>

    <input
      id="gist-share-url"
      type="text"
      data-autoselect
      class="form-control input-monospace input-sm"
      value="&lt;script src=&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808.js&quot;&gt;&lt;/script&gt;"
      aria-label="Clone this repository at &lt;script src=&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808.js&quot;&gt;&lt;/script&gt;"
      readonly>

    <div class="input-group-button">
      <clipboard-copy for="gist-share-url" aria-label="Copy to clipboard" class="btn btn-sm zeroclipboard-button" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;GIST&quot;,&quot;gist_id&quot;:16582398,&quot;client_id&quot;:&quot;1682679581.1547210180&quot;,&quot;originating_request_id&quot;:&quot;D408:62D1:4AB15A:82C4F4:5C9C9849&quot;,&quot;originating_url&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;referrer&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;user_id&quot;:415751}}" data-hydro-click-hmac="c6539af0e593551c307dbd9076bdf4c9d2ac23228a836810956ee613674e9608"><svg class="octicon octicon-clippy" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"/></svg></clipboard-copy>
    </div>
  </div>
</div>


    <div class="file-navigation-option">
</div>


    <div class="file-navigation-option">
      <a class="btn btn-sm" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;DOWNLOAD_ZIP&quot;,&quot;git_repository_type&quot;:&quot;GIST&quot;,&quot;gist_id&quot;:16582398,&quot;client_id&quot;:&quot;1682679581.1547210180&quot;,&quot;originating_request_id&quot;:&quot;D408:62D1:4AB15A:82C4F4:5C9C9849&quot;,&quot;originating_url&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;referrer&quot;:&quot;https://gist.github.com/JustinAzoff/37337b8dc70ca4da9808&quot;,&quot;user_id&quot;:415751}}" data-hydro-click-hmac="193979bbdad13511e9c3281cf5256b1b2e8f7d3fb282db4e03fa7c1ceb54d2d1" data-ga-click="Gist, download zip, location:gist overview" href="/JustinAzoff/37337b8dc70ca4da9808/archive/a57504e46a6e3b6697c9587626eb83ae70bdd826.zip">Download ZIP</a>
    </div>
  </div>
</div>


  </div>
</div>

<div class="container-lg px-3 new-discussion-timeline experiment-repo-nav">
  <div class="repository-content gist-content">
    
  <div>
    

        <div class="js-gist-file-update-container js-task-list-container file-box">
  <div id="file-is_file_growing-py" class="file">
      <div class="file-header">
        <div class="file-actions">

          <a class="btn btn-sm " href="/JustinAzoff/37337b8dc70ca4da9808/raw/a57504e46a6e3b6697c9587626eb83ae70bdd826/is_file_growing.py">Raw</a>
        </div>
        <div class="file-info">
          <span class="icon">
            <svg class="octicon octicon-gist" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.5 5L10 7.5 7.5 10l-.75-.75L8.5 7.5 6.75 5.75 7.5 5zm-3 0L2 7.5 4.5 10l.75-.75L3.5 7.5l1.75-1.75L4.5 5zM0 13V2c0-.55.45-1 1-1h10c.55 0 1 .45 1 1v11c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1zm1 0h10V2H1v11z"/></svg>
          </span>
          <a class="tooltipped tooltipped-s css-truncate" aria-label="Permalink" href="#file-is_file_growing-py">
            <strong class="user-select-contain gist-blob-name css-truncate-target">
              is_file_growing.py
            </strong>
          </a>
        </div>
      </div>
    

  <div itemprop="text" class="Box-body px-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="file-is_file_growing-py-L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="file-is_file_growing-py-LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="file-is_file_growing-py-LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="file-is_file_growing-py-LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="file-is_file_growing-py-LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> time</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="file-is_file_growing-py-LC5" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="file-is_file_growing-py-LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">SIZE_TIMEOUT</span> <span class="pl-k">=</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="file-is_file_growing-py-LC7" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="file-is_file_growing-py-LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_size</span>(<span class="pl-smi">f</span>):</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="file-is_file_growing-py-LC9" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> x <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">SIZE_TIMEOUT</span>):</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="file-is_file_growing-py-LC10" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="file-is_file_growing-py-LC11" class="blob-code blob-code-inner js-file-line">            size <span class="pl-k">=</span> os.stat(f).st_size</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="file-is_file_growing-py-LC12" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> size</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="file-is_file_growing-py-LC13" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">OSError</span>:</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="file-is_file_growing-py-LC14" class="blob-code blob-code-inner js-file-line">            time.sleep(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="file-is_file_growing-py-LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="file-is_file_growing-py-LC16" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> os.stat(f).st_size</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="file-is_file_growing-py-LC17" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="file-is_file_growing-py-LC18" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="file-is_file_growing-py-LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">is_growing</span>(<span class="pl-smi">f</span>):</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="file-is_file_growing-py-LC20" class="blob-code blob-code-inner js-file-line">    size <span class="pl-k">=</span> get_size(f)</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="file-is_file_growing-py-LC21" class="blob-code blob-code-inner js-file-line">    time.sleep(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="file-is_file_growing-py-LC22" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> x <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">SIZE_TIMEOUT</span>):</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="file-is_file_growing-py-LC23" class="blob-code blob-code-inner js-file-line">        time.sleep(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="file-is_file_growing-py-LC24" class="blob-code blob-code-inner js-file-line">        newsize <span class="pl-k">=</span> get_size(f)</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="file-is_file_growing-py-LC25" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> newsize <span class="pl-k">!=</span> size:</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="file-is_file_growing-py-LC26" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="file-is_file_growing-py-LC27" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="file-is_file_growing-py-LC28" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="file-is_file_growing-py-LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">is_growing_with_retries</span>(<span class="pl-smi">f</span>):</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="file-is_file_growing-py-LC30" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Check to see if a file is growing, with retries</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="file-is_file_growing-py-LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-s">       this should handle the case when a file gets rotated mid check</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="file-is_file_growing-py-LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="file-is_file_growing-py-LC33" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> x <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">3</span>):</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="file-is_file_growing-py-LC34" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> is_growing(f):</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="file-is_file_growing-py-LC35" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="file-is_file_growing-py-LC36" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="file-is_file_growing-py-LC37" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="file-is_file_growing-py-LC38" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="file-is_file_growing-py-LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="file-is_file_growing-py-LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="file-is_file_growing-py-LC41" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(sys.argv) <span class="pl-k">!=</span> <span class="pl-c1">2</span>:</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="file-is_file_growing-py-LC42" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Usage <span class="pl-c1">%s</span> filename<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> sys.argv[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="file-is_file_growing-py-LC43" class="blob-code blob-code-inner js-file-line">        sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="file-is_file_growing-py-LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="file-is_file_growing-py-LC45" class="blob-code blob-code-inner js-file-line">    f <span class="pl-k">=</span> sys.argv[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="file-is_file_growing-py-LC46" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="file-is_file_growing-py-LC47" class="blob-code blob-code-inner js-file-line">    res <span class="pl-k">=</span> is_growing_with_retries(f)</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="file-is_file_growing-py-LC48" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="file-is_file_growing-py-LC49" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> res:</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="file-is_file_growing-py-LC50" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> is not growing<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> f</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="file-is_file_growing-py-LC51" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-is_file_growing-py-L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="file-is_file_growing-py-LC52" class="blob-code blob-code-inner js-file-line">    sys.exit(<span class="pl-k">not</span> res)</td>
      </tr>
</table>


  </div>

  </div>
</div>


    <a name="comments"></a>
    <div class="discussion-timeline width-full js-quote-selection-container float-none" data-quote-markdown=".js-comment-body">
      <div class="js-discussion js-socket-channel" data-channel="marked-as-read:gist:16582398">
        

<!-- Rendered timeline since 2015-08-29 07:10:23 -->
<div id="partial-timeline-marker"
      class="js-timeline-marker js-updatable-content"
      data-url="/JustinAzoff/37337b8dc70ca4da9808/show_partial?partial=gist%2Ftimeline_marker&amp;since=1440857423"
      data-last-modified="Sat, 29 Aug 2015 14:10:23 GMT"
      >
</div>


        <div class="discussion-timeline-actions">
            <div class="timeline-comment-wrapper timeline-new-comment js-comment-container width-fit">
  <span class="timeline-comment-avatar "><a class="d-inline-block" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=415751" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/lhirlimann"><img class="avatar" src="https://avatars0.githubusercontent.com/u/415751?s=88&amp;v=4" width="44" height="44" alt="@lhirlimann" /></a></span>

  <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-new-comment-form js-needs-timeline-marker-header" action="/JustinAzoff/37337b8dc70ca4da9808/comments" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="3TmF9twyT/9M47qDdsaKfH1J3MS0Jdc9oJgtmqyhCTzMmJn7yP8jJEDjIelJNeq9PQNkFoX5HPc9UlVqvMbL4Q==" />
    <div class="timeline-comment">
      <div class="js-suggester-container js-previewable-comment-form previewable-comment-form write-selected" data-preview-url="/preview?markdown_unsupported=false&amp;subject=37337b8dc70ca4da9808&amp;subject_type=Gist" data-preview-authenticity-token="laz6jnssfXgsNxqftcOJ80Ivk/o3clngo6urTY7iVoccYem6ftuM3oMEqfslaGplZxxbsT7cGAx1rdKkExLEqg==">
  <div class="comment-form-head tabnav ">
      
<markdown-toolbar for="new_comment_field" class="toolbar-commenting ">
  <div class="toolbar-group">
    <md-header tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Add header text" data-ga-click="Markdown Toolbar, click, header">
      <svg class="octicon octicon-text-size" viewBox="0 0 18 16" version="1.1" width="18" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.62 9.08L12.1 3.66h-.06l-1.5 5.42h3.08zM5.7 10.13S4.68 6.52 4.53 6.02h-.08l-1.13 4.11H5.7zM17.31 14h-2.25l-.95-3.25h-4.07L9.09 14H6.84l-.69-2.33H2.87L2.17 14H0l3.3-9.59h2.5l2.17 6.34L10.86 2h2.52l3.94 12h-.01z"/></svg>
    </md-header>

    <md-bold tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Add bold text <ctrl+b>" data-ga-click="Markdown Toolbar, click, bold">
      <svg class="octicon octicon-bold" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1 2h3.83c2.48 0 4.3.75 4.3 2.95 0 1.14-.63 2.23-1.67 2.61v.06c1.33.3 2.3 1.23 2.3 2.86 0 2.39-1.97 3.52-4.61 3.52H1V2zm3.66 4.95c1.67 0 2.38-.66 2.38-1.69 0-1.17-.78-1.61-2.34-1.61H3.13v3.3h1.53zm.27 5.39c1.77 0 2.75-.64 2.75-1.98 0-1.27-.95-1.81-2.75-1.81h-1.8v3.8h1.8v-.01z"/></svg>
    </md-bold>

    <md-italic tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Add italic text <ctrl+i>" data-ga-click="Markdown Toolbar, click, italic">
      <svg class="octicon octicon-italic" viewBox="0 0 6 16" version="1.1" width="6" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2.81 5h1.98L3 14H1l1.81-9zm.36-2.7c0-.7.58-1.3 1.33-1.3.56 0 1.13.38 1.13 1.03 0 .75-.59 1.3-1.33 1.3-.58 0-1.13-.38-1.13-1.03z"/></svg>
    </md-italic>
  </div>

  <div class="toolbar-group">
    <md-quote tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Insert a quote" data-ga-click="Markdown Toolbar, click, quote">
      <svg class="octicon octicon-quote" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.16 3.5C3.73 5.06 2.55 6.67 2.55 9.36c.16-.05.3-.05.44-.05 1.27 0 2.5.86 2.5 2.41 0 1.61-1.03 2.61-2.5 2.61-1.9 0-2.99-1.52-2.99-4.25 0-3.8 1.75-6.53 5.02-8.42L6.16 3.5zm7 0c-2.43 1.56-3.61 3.17-3.61 5.86.16-.05.3-.05.44-.05 1.27 0 2.5.86 2.5 2.41 0 1.61-1.03 2.61-2.5 2.61-1.89 0-2.98-1.52-2.98-4.25 0-3.8 1.75-6.53 5.02-8.42l1.14 1.84h-.01z"/></svg>
    </md-quote>

    <md-code tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Insert code" data-ga-click="Markdown Toolbar, click, code">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
    </md-code>

    <md-link tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Add a link <ctrl+k>" data-ga-click="Markdown Toolbar, click, link">
      <svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"/></svg>
    </md-link>
  </div>

  <div class="toolbar-group">
    <md-unordered-list tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Add a bulleted list" data-ga-click="Markdown Toolbar, click, unordered list">
      <svg class="octicon octicon-list-unordered" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 13c0 .59 0 1-.59 1H.59C0 14 0 13.59 0 13c0-.59 0-1 .59-1h.81c.59 0 .59.41.59 1H2zm2.59-9h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1H4.59C4 2 4 2.41 4 3c0 .59 0 1 .59 1zM1.41 7H.59C0 7 0 7.41 0 8c0 .59 0 1 .59 1h.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm0-5H.59C0 2 0 2.41 0 3c0 .59 0 1 .59 1h.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm10 5H4.59C4 7 4 7.41 4 8c0 .59 0 1 .59 1h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm0 5H4.59C4 12 4 12.41 4 13c0 .59 0 1 .59 1h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01z"/></svg>
    </md-unordered-list>

    <md-ordered-list tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Add a numbered list" data-ga-click="Markdown Toolbar, click, ordered list">
      <svg class="octicon octicon-list-ordered" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12.01 13c0 .59 0 1-.59 1H4.6c-.59 0-.59-.41-.59-1 0-.59 0-1 .59-1h6.81c.59 0 .59.41.59 1h.01zM4.6 4h6.81C12 4 12 3.59 12 3c0-.59 0-1-.59-1H4.6c-.59 0-.59.41-.59 1 0 .59 0 1 .59 1zm6.81 3H4.6c-.59 0-.59.41-.59 1 0 .59 0 1 .59 1h6.81C12 9 12 8.59 12 8c0-.59 0-1-.59-1zm-9.4-6h-.72c-.3.19-.58.25-1.03.34V2h.75v2.14H.17V5h2.84v-.86h-1V1zm.392 8.12c-.129 0-.592.04-.802.07.53-.56 1.14-1.25 1.14-1.89C2.72 6.52 2.18 6 1.38 6c-.59 0-.97.2-1.38.64l.58.58c.19-.19.38-.38.64-.38.28 0 .48.16.48.52 0 .53-.77 1.2-1.7 2.06V10h3v-.88h-.598zm-.222 3.79v-.03c.44-.19.64-.47.64-.86 0-.7-.56-1.11-1.44-1.11-.48 0-.89.19-1.28.52l.55.64c.25-.2.44-.31.69-.31.27 0 .42.13.42.36 0 .27-.2.44-.86.44v.75c.83 0 .98.17.98.47 0 .25-.23.38-.58.38-.28 0-.56-.14-.81-.38l-.48.66c.3.36.77.56 1.41.56.83 0 1.53-.41 1.53-1.16 0-.5-.31-.81-.77-.94v.01z"/></svg>
    </md-ordered-list>

    <md-task-list tabindex="-1" class="toolbar-item tooltipped tooltipped-n" aria-label="Add a task list" data-ga-click="Markdown Toolbar, click, task list">
      <svg class="octicon octicon-tasklist" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15.41 9H7.59C7 9 7 8.59 7 8c0-.59 0-1 .59-1h7.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM9.59 4C9 4 9 3.59 9 3c0-.59 0-1 .59-1h5.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1H9.59zM0 3.91l1.41-1.3L3 4.2 7.09 0 8.5 1.41 3 6.91l-3-3zM7.59 12h7.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1H7.59C7 14 7 13.59 7 13c0-.59 0-1 .59-1z"/></svg>
    </md-task-list>
  </div>

  <div class="toolbar-group">
    <md-mention tabindex="-1" class="toolbar-item tooltipped tooltipped-nw" aria-label="Directly mention a user or team" data-ga-click="Markdown Toolbar, click, mention">
      <svg class="octicon octicon-mention" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.58 15c1.25 0 2.52-.31 3.56-.94l-.42-.94c-.84.52-1.89.83-3.03.83-3.23 0-5.64-2.08-5.64-5.72 0-4.37 3.23-7.18 6.58-7.18 3.45 0 5.22 2.19 5.22 5.2 0 2.39-1.34 3.86-2.5 3.86-1.05 0-1.36-.73-1.05-2.19l.73-3.75H8.98l-.11.72c-.41-.63-.94-.83-1.56-.83-2.19 0-3.66 2.39-3.66 4.38 0 1.67.94 2.61 2.3 2.61.84 0 1.67-.53 2.3-1.25.11.94.94 1.45 1.98 1.45 1.67 0 3.77-1.67 3.77-5C14 2.61 11.59 0 7.83 0 3.66 0 0 3.33 0 8.33 0 12.71 2.92 15 6.58 15zm-.31-5c-.73 0-1.36-.52-1.36-1.67 0-1.45.94-3.22 2.41-3.22.52 0 .84.2 1.25.83l-.52 3.02c-.63.73-1.25 1.05-1.78 1.05V10z"/></svg>
    </md-mention>

    <md-ref tabindex="-1" class="toolbar-item tooltipped tooltipped-nw" aria-label="Reference an issue or pull request" data-ga-click="Markdown Toolbar, click, reference">
      <svg class="octicon octicon-bookmark" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9 0H1C.27 0 0 .27 0 1v15l5-3.09L10 16V1c0-.73-.27-1-1-1zm-.78 4.25L6.36 5.61l.72 2.16c.06.22-.02.28-.2.17L5 6.6 3.12 7.94c-.19.11-.25.05-.2-.17l.72-2.16-1.86-1.36c-.17-.16-.14-.23.09-.23l2.3-.03.7-2.16h.25l.7 2.16 2.3.03c.23 0 .27.08.09.23h.01z"/></svg>
    </md-ref>

  </div>
</markdown-toolbar>

      <nav class="tabnav-tabs " role="tablist">
        <button type="button" class="btn-link tabnav-tab write-tab js-write-tab selected" role="tab" aria-selected="true">Write</button>
        <button type="button" class="btn-link tabnav-tab preview-tab js-preview-tab" role="tab">Preview</button>
      </nav>
  </div>


  <div class="comment-form-error js-comment-form-error" style="display:none">    There was an error creating your Gist.
</div>
  <file-attachment class="js-upload-markdown-image is-default" data-upload-policy-url="/upload/policies/assets" data-upload-policy-authenticity-token="fywSfqbX/qMtKIMDNAygkY5x7qxgohBtmlPBBKx0chp0mrYHuh4cZLpxqGRF/8mUKQrfDZQZQuIgChAc9fqIIw==">
    <div class="write-content js-write-bucket upload-enabled  js-reaction-suggestion tooltipped tooltipped-ne tooltipped-no-delay tooltipped-align-left-1 hide-reaction-suggestion" data-reaction-markup="Would you like to leave a reaction instead?">


      <textarea name="comment[body]"
                id="new_comment_field"
                
                placeholder="Leave a comment"
                aria-label="Comment body"
                class="form-control input-contrast comment-form-textarea js-comment-field js-paste-markdown js-task-list-field js-quick-submit js-size-to-fit js-suggester-field js-session-resumable "
                ></textarea>
        
  <p class="drag-and-drop position-relative">
    <input accept=".gif,.jpeg,.jpg,.png" type="file"
      multiple="multiple"
      class="manual-file-chooser top-0 right-0 bottom-0 left-0 width-full ml-0 js-manual-file-chooser form-control"
      style="opacity: 0.1; min-height: 0;"
      aria-label="Attach files to your comment">
    <span class="bg-gray-light position-absolute top-0 left-0 width-full height-full rounded-1" style="pointer-events: none;"></span>
    <span class="position-relative" style="pointer-events: none;">
      <span class="default">
          Attach files by dragging &amp; dropping, selecting or pasting them.
      </span>
      <span class="loading">
        <img alt="" width="16" height="16" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" /> Uploading your files…
      </span>
      <span class="error bad-file">
        We don’t support that file type.
        <span class="drag-and-drop-error-info">
          <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a
          GIF, JPEG, JPG or PNG.
        </span>
      </span>
      <span class="error bad-permissions">
        Attaching documents requires write permission to this repository.
        <span class="drag-and-drop-error-info">
          <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a GIF, JPEG, JPG or PNG.
        </span>
      </span>
      <span class="error repository-required">
        We don’t support that file type.
        <span class="drag-and-drop-error-info">
          <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a GIF, JPEG, JPG or PNG.
        </span>
      </span>
      <span class="error too-big">
        Yowza, that’s a big file
        <span class="drag-and-drop-error-info">
          <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a file smaller than 10MB.
        </span>
      </span>
      <span class="error empty">
        This file is empty.
        <span class="drag-and-drop-error-info">
          <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a file that’s not empty.
        </span>
      </span>
      <span class="error hidden-file">
        This file is hidden.
        <span class="drag-and-drop-error-info">
          <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with another file.
        </span>
      </span>
      <span class="error failed-request">
        Something went really wrong, and we can’t process that file.
        <span class="drag-and-drop-error-info">
          <button type="button" class="btn-link manual-file-chooser-text">Try again.</button>
        </span>
      </span>
    </span>
  </p>


      <div class="suggester-container">
        <div class="suggester js-suggester js-navigation-container"
             data-url="/JustinAzoff/37337b8dc70ca4da9808/suggestions"
             hidden>
        </div>
      </div>
    </div>
</file-attachment>
  <div class="preview-content overflow-auto border-bottom">
    <input type="hidden" name="original-line" value="" class="js-original-line">
    <input type="hidden" name="path" value="" class="js-path">
    <input type="hidden" name="line" value="" class="js-line-number">
    <div class="comment js-suggested-changes-container" data-thread-side="">
  <div class="comment-body markdown-body js-preview-body">
    <p>Nothing to preview</p>
  </div>
</div>

  </div>

      <div class="float-left ">
        <a class="tabnav-extra " href="https://guides.github.com/features/mastering-markdown/" target="_blank" data-ga-click="Markdown Toolbar, click, help">
          <svg class="octicon octicon-markdown v-align-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14.85 3H1.15C.52 3 0 3.52 0 4.15v7.69C0 12.48.52 13 1.15 13h13.69c.64 0 1.15-.52 1.15-1.15v-7.7C16 3.52 15.48 3 14.85 3zM9 11H7V8L5.5 9.92 4 8v3H2V5h2l1.5 2L7 5h2v6zm2.99.5L9.5 8H11V5h2v3h1.5l-2.51 3.5z"/></svg>
          Styling with Markdown is supported
        </a>
      </div>


  <div class="comment-form-error comment-form-bottom js-comment-update-error"></div>
</div>


      <div class="form-actions">
        <div id="partial-new-comment-form-actions">
  <button type="submit" class="btn btn-primary" data-disable-with data-disable-invalid>
    Comment
  </button>
</div>

      </div>
    </div>
</form></div>

        </div>
      </div>
    </div>
</div>
  </div>

  <div class="modal-backdrop js-touch-events"></div>
</div><!-- /.container -->

    </main>
  </div>

  </div>

        
<div class="footer container-lg width-full px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2019 <span title="0.14480s from unicorn-6958b7f4b6-9brd6">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-jFuNBkwlIX73xJbI2nTCs01W/xjwP+Ccc0gEdkD4d/tQBv4xIZx4dZLnkYhzawWhnxjJbvkHsxSXQffNs0Ce4Q==" type="application/javascript" src="https://github.githubassets.com/assets/compat-bootstrap-8102d067.js"></script>
    <script crossorigin="anonymous" integrity="sha512-XfAj4ST+jv9o5wjFN44XkrvsfCnrQFO87qONf4TUQgWyAF0YEVXU/wSzOilSD3ZqB9RjphqmDeTw6koXDtrJKQ==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-74fc03d0.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-ELcoQzvMh1v0n9tV0v4DZxtFa46TCS7cmssLC00qGX9qWsD82GDH4PZEu/ShNNqIdwXCCuRptNs3IQ8QuHqqIA==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-be1f09c7.js"></script>
    
      <script crossorigin="anonymous" async="async" integrity="sha512-jBy3hBXaLVuYqRVwrsrPgPLlCW0l5AGJlwzPQxUwEC3K2tv+//lHCEB1NQYn48PHevZAk1iIRuOovfX1QG4akw==" type="application/javascript" src="https://github.githubassets.com/assets/gist-bootstrap-e61e3122.js"></script>

    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

