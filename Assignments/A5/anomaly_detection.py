<!DOCTYPE html><html>
<head>
    <title>Sign In - CAS &#8211; Central Authentication Service</title>
    <meta charset="UTF-8"/><meta http-equiv="X-UA-Compatible" content="IE=edge"/><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/><link rel="stylesheet" href="/cas/webjars/font-awesome/5.0.13/web-fonts-with-css/css/fontawesome-all.min.css"/><link type="text/css" rel="stylesheet" href="/cas/webjars/lato/0.3.0/css/lato.min.css"/><link rel="stylesheet" href="/cas/css/cas.css"/><link rel="shortcut icon" href="/cas/images/favicon.ico" /><script type="text/javascript" src="/cas/webjars/jquery/3.3.1/jquery.min.js"></script>

    
    <link  href="/cas/css/sfu-overlay.css" rel="stylesheet"/><script src="/cas/js/sfu-overlay.js" type="text/javascript"></script>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/><meta charset="utf-8" http-equiv="refresh" content="300;url=../lt-timeout.html" /></head>

<body class="login">
<header role="banner">
        <div class="grid sfu-header">
            <div class="row">
                <div class="col sm-12">
                    <a href="http://www.sfu.ca">
                        <div class="sfu-logo"><h1>Simon Fraser University</h1></div>
                    </a>
                    <div class="sfu-service-name">
                        <h1>CourSys</h1>
                        </div>
                </div>
            </div>
            <div class="row sm-banner"></div>
        </div>
    </header>

<main role="main" class="container mt-3 mb-3">
    <div id="content" class="row">
        <div class="col-lg">
            <div class="card form-background">
                <div class="sfu-login-form">
                    <div class="card-header text-center">
                        <h2>Sign In</h2>
                        <span class="fa-stack fa-2x hidden-xs">
                        <i class="fa fa-circle fa-stack-2x"></i>
                        <i class="fa fa-lock fa-stack-1x fa-inverse"></i>
                        </span>
                    </div>
                    <div class="card-body">
                        <form method="post" id="fm1" action="login">
                            <section class="form-group">
                                <label for="username"><span class="accesskey">U</span>sername:</label>

                                <div>
                                    <input class="form-control required"
                                        id="username"
                                        size="25"
                                        tabindex="1"
                                        type="text"
                                        accesskey="u"
                                        autocomplete="off" name="username" value=""/></div>
                            </section>

                            <section class="form-group">
                                <label for="password"><span class="accesskey">P</span>assword:</label>

                                <div>
                                    <input class="form-control required"
                                        type="password"
                                        id="password"
                                        size="25"
                                        tabindex="2"
                                        accesskey="p"
                                        autocomplete="off" name="password" value=""/><span id="capslock-on" style="display:none;">
                                    <p>
                                        <i class="fa fa-exclamation-circle"></i>
                                        <span>CAPSLOCK key is turned on!</span>
                                    </p>
                                </span>
                                </div>
                            </section>

                            <input type="hidden" name="execution" value="d9624d97-e2a3-4211-9e87-8d9ac112503e_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"/><input type="hidden" name="_eventId" value="submit"/><input type="hidden" name="geolocation"/><input class="btn btn-block btn-submit"
                                name="submit"
                                accesskey="l"
                                tabindex="6"
                                type="submit"
                                value="Sign In"
                            /></form>
                    </div>
                </div>
                <div class="sfu-password-information">
                    <div>
                        <span class="fa fa-question-circle"></span>
                        <span>Forgot your <a href="https://my.sfu.ca/ForgotPassword">password</a> or <a href="https://my.sfu.ca/ForgotUsername">computing ID</a>?<br /><a href="https://my.sfu.ca/ChangePassword">Change your password</a><br /><a href="http://www.sfu.ca/itservices.html">Need help?</a></span>
                        <p/></div>

                    <script type="text/javascript">
                        var i = "One moment please..."
                        $( document ).ready(function() {
                            $("#fm1").submit(function () {
                                $(":submit").attr("disabled", true);
                                $(":submit").attr("value", i);
                                console.log(i);
                                return true;
                            });
                        });
                    </script>

                    <div id="sidebar">
        <div class="sidebar-content">
            <p><h4>Protect your Password</h4><p>SFU will never request our users provide or confirm their Computing ID or password via email or by going to any web site. SFU users should ignore all messages requesting Computing ID and/or password information, no matter how authentic they may appear. <a href="https://www.sfu.ca/itservices/info_security/phishing_scams.html">More information on phishing</a>.</p><p>Always check that your browser shows a closed lock icon and that the URL of this page starts with <strong>https://cas.sfu.ca</strong> and not some other address.</p><p>If you're not sure, <strong>do not enter your password.</strong></p></p>
        </div>
    </div>
                </div>
            </div>
        </div>
        <!--
        <div th:replace="fragments/serviceui :: serviceUI">
            <a href="fragments/serviceui.html">service ui fragment</a>
        </div>
        --><!--
        <div id="notices" class="col-md mt-3 mt-md-0"  th:if="${delegatedAuthenticationProviderDominant == null}">
            <div th:replace="fragments/insecure :: insecure">
                <a href="fragments/insecure.html">insecure alert goeshere</a>
            </div>
            <div th:replace="fragments/defaultauthn :: staticAuthentication">
                <a href="fragments/defaultauthn.html">defaultAuthn</a>
            </div>
            <div th:replace="fragments/cookies :: cookiesDisabled">
                <a href="fragments/cookies.html">cookies fragment</a>
            </div>
            <div th:replace="fragments/serviceui :: serviceUI">
                <a href="fragments/serviceui.html">service ui fragment</a>
            </div>
            <div th:replace="fragments/cas-resources-list :: cas-resource-list">
                <a href="fragments/cas-resources-list.html">cas-resource</a> list fragment
            </div>
        </div>
        <div id="providers" class="col-md mt-3 mt-md-0">
            <div th:replace="fragments/loginProviders :: loginProviders">
                <a href="fragments/loginProviders.html">loginProviders</a>
            </div>
        </div>
        --></div>
</main>

<footer class="footer" role="contentinfo">
        <div class="sfu-home-links">
            <h4><a href="https://www.sfu.ca/itservices/publishing/publish_howto/enhanced_web_publishing/cas1.html">IT Services</a></h4>
            <ul>
                <li><a href="https://www.sfu.ca/main/admission.html">Admission</a></li>
                <li><a href="https://www.sfu.ca/main/programs.html">Programs</a></li>
                <li><a href="https://www.sfu.ca/main/learning.html">Learning</a></li>
                <li><a href="https://www.sfu.ca/main/research-at-sfu.html">Research</a></li>
                <li><a href="https://www.sfu.ca/main/sfu-community.html">Community</a></li>
                <li><a href="https://www.sfu.ca/main/about.html">About</a></li>
            </ul>
        </div>
        <div class="sfu-contact">
            <h4>Contact Us</h4>
            <p><strong>IT Services</strong></p>
            <p>
                Strand Hall 1001<br />
                8888 University Drive<br />
                Burnaby, B.C.<br />
                Canada. V5A 1S6
            </p>
        </div>

        <div class="sfu-links">
            <div class="h-line"></div>
            <ul>
                <li><a href="https://www.sfu.ca/srs">Safety &amp; Risk</a></li>
                <li><a href="https://www.sfu.ca/campuses/maps-and-directions">SFU Maps &amp; Directions</a></li>
                <li><a href="https://www.sfu.ca/admission">SFU Admissions</a></li>
                <li><a href="http://www.sfu.ca/security/sfuroadconditions/">Road Report</a></li>
                <li><a href="https://give.sfu.ca">Give to SFU</a></li>
                <li><a href="https://www.sfu.ca/contact/terms-conditions">Terms and conditions</a></li>
                <li><a href="https://www.sfu.ca/" class="muted">© Simon Fraser University</a></li>
            </ul>
        </div>
        <div class="sfu-logo-acknowledge">
            <img src="/cas/images/logo-stacked.png" id="footer-logo-img" alt=""><p style="color:#eee;">We would like to acknowledge that at Simon Fraser University we live and work on the unceded traditional territories of the Coast Salish peoples of the Musqueam, Squamish, and Tsleil-Waututh&nbsp;Nations.</p>
        </div>
                
    </footer>

<script type="text/javascript" src="/cas/webjars/zxcvbn/4.3.0/zxcvbn.js"></script>
<script type="text/javascript" src="/cas/webjars/jquery-ui/1.12.1/jquery-ui.min.js"></script>
<script type="text/javascript" src="/cas/webjars/jquery-cookie/1.4.1-1/jquery.cookie.js"></script>
<script src="/cas/webjars/bootstrap/4.1.0/js/bootstrap.bundle.min.js"></script>

<script src="/cas/webjars/headjs/1.0.3/head.min.js"></script>
<script src="/cas/webjars/store.js/1.3.17/store.min.js"></script>
<script type="text/javascript" src="/cas/js/cas.js"></script>

<script>
head.ready(document, function () {
    if (!window.jQuery) {
    	var jqueryUrl = "\/cas\/webjars\/jquery\/3.3.1\/jquery.min.js"; 
        head.load(jqueryUrl, loadjQueryUI);
    } else {
        notifyResourcesAreLoaded(resourceLoadedSuccessfully);
    }
});

function loadjQueryUI() {
	var jqueryUrl = "\/cas\/webjars\/jquery-ui\/1.12.1\/jquery-ui.min.js"; 
	head.load(jqueryUrl, loadjQueryCookies);
}

function loadjQueryCookies() {
	var jqueryUrl = "\/cas\/webjars\/jquery-cookie\/1.4.1-1\/jquery.cookie.js"; 
	head.load(jqueryUrl, notifyResourcesAreLoaded(resourceLoadedSuccessfully));
}

function notifyResourcesAreLoaded(callback) {
    if (typeof callback === "function") {
        callback();
    }
}
</script>

<script>
    /*<![CDATA[*/

    var trackGeoLocation = false;

    var googleAnalyticsTrackingId = null;

    if (googleAnalyticsTrackingId != null && googleAnalyticsTrackingId != '') {
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

        ga('create', googleAnalyticsTrackingId, 'auto');
        ga('send', 'pageview');
    }

    /*]]>*/
</script>

<!-- /*Fragment for template-specific includes */--></body>
</html>
