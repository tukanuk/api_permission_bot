from bs4 import BeautifulSoup

text = """
<!DOCTYPE html>
<html lang="en">
<head data-id="api-metrics-v2-get-all">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta property="publish_date" content="2019-06-26T10:00:38+00:00">
  <meta property="modified_date" content="2020-06-26T11:21:54+00:00">
  <link rel="preconnect" href="https://dt-cdn.net" crossorigin="">
  <link rel="preconnect" href="https://www.google-analytics.com" crossorigin="">
  <title>Metrics API - GET metrics | Dynatrace Help</title>
  <meta name="description" content="Learn how you can use the Dynatrace API to retrieve the metrics of monitored entities.">
  <link rel="stylesheet" href="/support/doc/common/css/main-a957f7b64c.css">
  <link href="/support/doc/common/css/print-2abfe72e8a.css" rel="stylesheet" media="print" type="text/css">
  
  <link rel="canonical" href="https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/">
  <link rel="alternate" type="application/rss+xml" title="Metrics API - GET metrics" href="https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/feed.xml">
  <script>document.documentElement.className += ' js';</script>
  <script type="text/javascript">
    var dynatraceFont = dynatraceFont || {};
    dynatraceFont.storeKeyOld = 'fcache';
    dynatraceFont.storeKey = 'fcacheV2'
  
    dynatraceFont.addStyles = function addStyles(fonts) {
      if(document.getElementById('font-css') !== null) {
        return;
      }
      var scriptElem = document.getElementsByTagName('script')[0];
      var styleTag = document.createElement('style');
      styleTag.id = 'font-css';
      styleTag.setAttribute('type', 'text/css');
      styleTag.innerHTML = fonts;
      scriptElem.parentNode.insertBefore(styleTag, scriptElem);
    }
  
    if (localStorage.getItem(dynatraceFont.storeKey) !== null) {
      dynatraceFont.addStyles(localStorage.getItem(dynatraceFont.storeKey));
    }
  </script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.13.1/styles/atom-one-dark-reasonable.min.css" rel="stylesheet" type="text/css">

  <link rel="apple-touch-icon" sizes="57x57" href="https://dt-cdn.net/images/apple-touch-icon-57x57-57-1fffb01d7e.png">
  <link rel="apple-touch-icon" sizes="60x60" href="https://dt-cdn.net/images/apple-touch-icon-60x60-60-d9a138c712.png">
  <link rel="apple-touch-icon" sizes="72x72" href="https://dt-cdn.net/images/apple-touch-icon-72x72-72-904fd0a540.png">
  <link rel="apple-touch-icon" sizes="76x76" href="https://dt-cdn.net/images/apple-touch-icon-76x76-76-9f8edcd3fc.png">
  <link rel="apple-touch-icon" sizes="114x114" href="https://dt-cdn.net/images/apple-touch-icon-114x114-114-145c74b2f0.png">
  <link rel="apple-touch-icon" sizes="120x120" href="https://dt-cdn.net/images/apple-touch-icon-120x120-120-3897b7214b.png">
  <link rel="apple-touch-icon" sizes="144x144" href="https://dt-cdn.net/images/apple-touch-icon-144x144-144-4cf0d2af93.png">
  <link rel="apple-touch-icon" sizes="152x152" href="https://dt-cdn.net/images/apple-touch-icon-152x152-152-0eb753d535.png">
  <link rel="apple-touch-icon" sizes="180x180" href="https://dt-cdn.net/images/apple-touch-icon-180x180-180-80738a22c0.png">
  <link rel="icon" href="https://dt-cdn.net/images/favicon-32x32-32-26d70a5cff.png">
  <meta name="apple-mobile-web-app-title" content="Dynatrace">
  <meta name="application-name" content="Dynatrace">
  <meta name="msapplication-TileColor" content="#454646">
  <meta name="msapplication-TileImage" content="https://dt-cdn.net/images/mstile-144x144-144-501f48f393.png">
  <meta name="theme-color" content="#ffffff">  <meta property="og:type" content="article">
  <meta property="og:title" content="Metrics API - GET metrics | Dynatrace Help">
  <meta property="og:description" content="Learn how you can use the Dynatrace API to retrieve the metrics of monitored entities.">
  <meta property="og:url" content="https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/">
  <meta property="og:site_name" content="Dynatrace">
  <meta property="og:image" content="">
  <meta property="article:publisher" content="https://www.facebook.com/Dynatrace/">
  <meta property="fb:app_id" content="1221150274658460">
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:description" content="Learn how you can use the Dynatrace API to retrieve the metrics of monitored entities.">
  <meta property="twitter:title" content="Metrics API - GET metrics | Dynatrace Help">
  <meta property="twitter:site" content="@Dynatrace">
  <meta property="twitter:image" content="">
  <meta property="twitter:creator" content="@Dynatrace">
  <script type="text/javascript" src="/ruxitagentjs_ICA2SVfqru_10195200709173710.js" data-dtconfig="rid=RID_-1957095447|rpid=-1249388886|domain=dynatrace.com|reportUrl=/rb_bf25977vwq|app=7fb64fd3b202c513|cuc=4mvph58u|featureHash=ICA2SVfqru|lastModification=1594380987569|useNewCookies=1|dtVersion=10195200709173710|tp=500,50,0,1|rdnt=1|uxrgce=1|uxdcw=1500|vs=2|agentUri=/ruxitagentjs_ICA2SVfqru_10195200709173710.js"></script><script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@id": "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/#webpage",
    "@type": "WebPage",
    "url": "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/",
    "name": "Dynatrace"
  }
  </script>
  <script type="application/ld+json">
   {
    "@context": "http://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement":
    [
      {
       "@type": "ListItem",
       "position": 0,
       "item":
       {
        "@id": "https://www.dynatrace.com/",
        "name": "Dynatrace",
        "image": ""
        }
      },
      {
       "@type": "ListItem",
       "position": 1,
       "item":
       {
        "@id": "https://www.dynatrace.com/support/",
        "name": "Support",
        "image": ""
        }
      },
      {
       "@type": "ListItem",
       "position": 2,
       "item":
       {
        "@id": "https://www.dynatrace.com/support/help/",
        "name": "Home",
        "image": ""
        }
      },
      {
       "@type": "ListItem",
       "position": 3,
       "item":
       {
        "@id": "https://www.dynatrace.com/support/help/dynatrace-api/",
        "name": "Dynatrace API",
        "image": ""
        }
      },
      {
       "@type": "ListItem",
       "position": 4,
       "item":
       {
        "@id": "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/",
        "name": "Environment API",
        "image": ""
        }
      },
      {
       "@type": "ListItem",
       "position": 5,
       "item":
       {
        "@id": "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/",
        "name": "Metrics API v2",
        "image": ""
        }
      },
      {
       "@type": "ListItem",
       "position": 6,
       "item":
       {
        "@id": "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/",
        "name": "Metrics API - GET metrics",
        "image": ""
        }
      }
    ]
   }
  </script>
</head>
  <body>

    <div class="nav">
      <a class="sr-only" href="https://www.dynatrace.com/">Dynatrace.com Homelink</a>
      <button class="nav__toggle js-nav-toggle">
        <img src="https://dt-cdn.net/images/nav-mobile-trigger-66de6f5305.svg" alt="Nav toggle" sizes="(min-width: 992px) 50vw, 100vw">
      </button>
      <nav id="nav-bar" class="nav__bar">
        <ul class="nav__list nav__list--primary">  
          <li class="nav__item  expandable expandable--nav">
            <a class="nav__link  expandable__trigger" href="https://www.dynatrace.com/platform/">Platform</a>
            
            <div class="nav__secondary expandable__content">
    
              <ul class="nav__list nav__list--secondary">
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/platform/">Overview</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/technologies/">Supported technologies</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/pricing/">Pricing</a>
                </li>
              </ul>
                <div class="nav__secondary__promos">
                    <div class="nav__secondary__promo__item nav__secondary__promo__item--small">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/platform/application-performance-monitoring/">
                        <img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/icon-apm-707c647d9b.svg" alt="Application performance decoration image" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw">
                        <span class="nav__secondary__promo__label">Application performance</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item nav__secondary__promo__item--small">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/platform/infrastructure-monitoring/">
                        <img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/cloud-monitoring-40x40-white-875195d746.svg" alt="Infrastructure monitoring decoration image" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw">
                        <span class="nav__secondary__promo__label">Infrastructure monitoring</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item nav__secondary__promo__item--small">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/platform/aiops/">
                        <img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/aiops-40x40-white-c91b037395.svg" alt="AIOps decoration image" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw">
                        <span class="nav__secondary__promo__label">AIOps</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item nav__secondary__promo__item--small">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/platform/digital-experience-monitoring/">
                        <img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/dem-new-40x40-white-784344eea7.svg" alt="Digital experience decoration image" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw">
                        <span class="nav__secondary__promo__label">Digital experience</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item nav__secondary__promo__item--small">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/platform/digital-business-analytics/">
                        <img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/icon-dba-aae6c1acda.svg" alt="Digital business analytics decoration image" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw">
                        <span class="nav__secondary__promo__label">Digital business analytics</span>
                      </a>
                    </div>
                </div>
            </div>
    
          </li>
          <li class="nav__item  expandable expandable--nav">
            <a class="nav__link  expandable__trigger" href="https://www.dynatrace.com/solutions/">Solutions</a>
            
            <div class="nav__secondary expandable__content">
    
              <ul class="nav__list nav__list--secondary">
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/solutions/">Overview</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/technologies/aws-monitoring/">AWS</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/technologies/azure-monitoring/">Azure</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/technologies/google-cloud-monitoring/">Google</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/technologies/kubernetes-monitoring/">Kubernetes</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/technologies/openshift-monitoring/">OpenShift</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/integrations/servicenow/">ServiceNow</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/technologies/vmware-tanzu-monitoring/">VMware Tanzu</a>
                </li>
              </ul>
                <div class="nav__secondary__promos">
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/digital-transformation/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/dth-promo-200-b4dfd74abe.webp 200w, https://dt-cdn.net/images/dth-promo-400-b4dfd74abe.webp 400w, https://dt-cdn.net/images/dth-promo-600-b4dfd74abe.webp 600w, https://dt-cdn.net/images/dth-promo-800-b4dfd74abe.webp 800w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/dth-promo-800-b4dfd74abe.jpg" alt="Digital Transformation Hub decoration image" srcset="https://dt-cdn.net/images/dth-promo-200-b4dfd74abe.jpg 200w, https://dt-cdn.net/images/dth-promo-400-b4dfd74abe.jpg 400w, https://dt-cdn.net/images/dth-promo-600-b4dfd74abe.jpg 600w, https://dt-cdn.net/images/dth-promo-800-b4dfd74abe.jpg 800w" width="800px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">Digital Transformation Hub</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/company/customers/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/customer-promo-200-b11cc4f062.webp 200w, https://dt-cdn.net/images/customer-promo-267-b11cc4f062.webp 267w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/customer-promo-267-b11cc4f062.jpg" alt="Customer stories decoration image" srcset="https://dt-cdn.net/images/customer-promo-200-b11cc4f062.jpg 200w, https://dt-cdn.net/images/customer-promo-267-b11cc4f062.jpg 267w" width="267px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">Customer stories</span>
                      </a>
                    </div>
                </div>
            </div>
    
          </li>
          <li class="nav__item  expandable expandable--nav">
            <a class="nav__link  expandable__trigger" href="https://www.dynatrace.com/news/">News</a>
            
            <div class="nav__secondary expandable__content">
    
              <ul class="nav__list nav__list--secondary">
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/">Overview</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/blog/">Blog</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/event/">Events</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/webinar/">Webinars</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/newsroom/">Newsroom</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/pureperformance/">Podcasts</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/product-news/">Product news</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/news/resource/">Resources</a>
                </li>
              </ul>
                <div class="nav__secondary__promos">
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/digital-transformation/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/dth-promo-200-b4dfd74abe.webp 200w, https://dt-cdn.net/images/dth-promo-400-b4dfd74abe.webp 400w, https://dt-cdn.net/images/dth-promo-600-b4dfd74abe.webp 600w, https://dt-cdn.net/images/dth-promo-800-b4dfd74abe.webp 800w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/dth-promo-800-b4dfd74abe.jpg" alt="Digital Transformation Hub decoration image" srcset="https://dt-cdn.net/images/dth-promo-200-b4dfd74abe.jpg 200w, https://dt-cdn.net/images/dth-promo-400-b4dfd74abe.jpg 400w, https://dt-cdn.net/images/dth-promo-600-b4dfd74abe.jpg 600w, https://dt-cdn.net/images/dth-promo-800-b4dfd74abe.jpg 800w" width="800px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">Digital Transformation Hub</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/covid-19-response/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/dynatrace-product-200-6b73761432.webp 200w, https://dt-cdn.net/images/dynatrace-product-267-6b73761432.webp 267w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/dynatrace-product-267-6b73761432.jpg" alt="COVID-19 Continuity Support decoration image" srcset="https://dt-cdn.net/images/dynatrace-product-200-6b73761432.jpg 200w, https://dt-cdn.net/images/dynatrace-product-267-6b73761432.jpg 267w" width="267px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">COVID-19 Continuity Support</span>
                      </a>
                    </div>
                </div>
            </div>
    
          </li>
          <li class="nav__item  expandable expandable--nav">
            <a class="nav__link  expandable__trigger" href="https://www.dynatrace.com/company/">Company</a>
            
            <div class="nav__secondary expandable__content">
    
              <ul class="nav__list nav__list--secondary">
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/company/">Overview</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/company/customers/">Customer stories</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/company/careers/">Careers</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/partners/">Partners</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/company/leadership/">Leadership</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://ir.dynatrace.com/">Investor Relations</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/company/locations/">Locations</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/contact/">Contact</a>
                </li>
              </ul>
                <div class="nav__secondary__promos">
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/covid-19-response/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/dynatrace-product-200-6b73761432.webp 200w, https://dt-cdn.net/images/dynatrace-product-267-6b73761432.webp 267w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/dynatrace-product-267-6b73761432.jpg" alt="COVID-19 Continuity Support decoration image" srcset="https://dt-cdn.net/images/dynatrace-product-200-6b73761432.jpg 200w, https://dt-cdn.net/images/dynatrace-product-267-6b73761432.jpg 267w" width="267px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">COVID-19 Continuity Support</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/company/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/reinvention-200-a94daf4a98.webp 200w, https://dt-cdn.net/images/reinvention-267-a94daf4a98.webp 267w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/reinvention-267-a94daf4a98.jpg" alt="Our reinvention decoration image" srcset="https://dt-cdn.net/images/reinvention-200-a94daf4a98.jpg 200w, https://dt-cdn.net/images/reinvention-267-a94daf4a98.jpg 267w" width="267px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">Our reinvention</span>
                      </a>
                    </div>
                </div>
            </div>
    
          </li>
          <li class="nav__item  expandable expandable--nav">
            <a class="nav__link  expandable__trigger" href="https://www.dynatrace.com/services-support/">Services &amp; support</a>
            
            <div class="nav__secondary expandable__content">
    
              <ul class="nav__list nav__list--secondary">
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/services-support/">Overview</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/services-support/dynatrace-one/">Dynatrace ONE</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/services-support/expert-services/">Expert Services</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://university.dynatrace.com">University</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/services-support/#support-resources-section">Support</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/services-support/business-insights/">Business Insights</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/services-support/autonomous-cloud-enablement/">ACE</a>
                </li>
                <li class="nav__item">
                  <a class="nav__link" href="https://www.dynatrace.com/covid-19-response/">COVID-19 Continuity Support</a>
                </li>
              </ul>
                <div class="nav__secondary__promos">
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/services-support/adopt/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/careers-team-200-a595c7e8c3.webp 200w, https://dt-cdn.net/images/careers-team-267-a595c7e8c3.webp 267w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/careers-team-267-a595c7e8c3.jpg" alt="Adopt Dynatrace decoration image" srcset="https://dt-cdn.net/images/careers-team-200-a595c7e8c3.jpg 200w, https://dt-cdn.net/images/careers-team-267-a595c7e8c3.jpg 267w" width="267px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">Adopt Dynatrace</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/services-support/accelerate/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/services-promo-200-c2b2b1a94d.webp 200w, https://dt-cdn.net/images/services-promo-267-c2b2b1a94d.webp 267w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/services-promo-267-c2b2b1a94d.jpg" alt="Accelerate Software Delivery decoration image" srcset="https://dt-cdn.net/images/services-promo-200-c2b2b1a94d.jpg 200w, https://dt-cdn.net/images/services-promo-267-c2b2b1a94d.jpg 267w" width="267px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">Accelerate Software Delivery</span>
                      </a>
                    </div>
                    <div class="nav__secondary__promo__item ">
                      <a class="nav__secondary__promo__link" href="https://www.dynatrace.com/services-support/automate/">
                        <picture><source type="image/webp" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw" srcset="https://dt-cdn.net/images/support-headset-200-1de3c9ef38.webp 200w, https://dt-cdn.net/images/support-headset-267-1de3c9ef38.webp 267w"><img class="nav__secondary__promo__image" src="https://dt-cdn.net/images/support-headset-267-1de3c9ef38.jpg" alt="Automate Cloud Operations decoration image" srcset="https://dt-cdn.net/images/support-headset-200-1de3c9ef38.jpg 200w, https://dt-cdn.net/images/support-headset-267-1de3c9ef38.jpg 267w" width="267px" sizes="((min-width: 992px) and (not (media: print))) 50vw, 100vw"></picture>
                        <span class="nav__secondary__promo__label">Automate Cloud Operations</span>
                      </a>
                    </div>
                </div>
            </div>
    
          </li>
          <li class="nav__item nav__item--right">
            <a class="nav__link nav__search" href="https://search.dynatrace.com">
              <svg width="16" height="16" viewbox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                <path d="M6.368.5a5.868 5.868 0 1 0-.153 11.735A5.868 5.868 0 0 0 6.368.5zm0 10.1a4.237 4.237 0 0 1-4.233-4.232 4.237 4.237 0 0 1 4.233-4.233A4.237 4.237 0 0 1 10.6 6.368 4.237 4.237 0 0 1 6.368 10.6z M15.372 13.724l-5.181-5.18a7.024 7.024 0 0 1-1.648 1.647l5.181 5.181c.171.17.448.17.618 0l1.03-1.03a.437.437 0 0 0 0-.618z"/>
              </svg> 
            </a>
          </li>
          <li class="nav__item nav__item--right">
            <a class="nav__link" href="https://sso.dynatrace.com/">SaaS login</a>
          </li>
        </ul>
      </nav>
      <div class="nav__brand" aria-hidden="true">
        <a class="nav__brand__link" href="https://www.dynatrace.com/">
          <svg class="nav__logo" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 800 142">
              <path class="nav__logo__text" d="M578.6 37.2h-18.4c-5.2 0-8.8 1-11 3.2-2.2 2.1-3.3 5.8-3.3 10.8v63.6h-11V50.4c.1-4.9.9-10.2 3.5-14.2 4.7-7.5 13.7-8.9 20.4-8.9h19.9v9.9zm-71 67.6c-5.2 0-8.8-1-11-3.2-2.2-2.1-3.3-5.6-3.3-10.6V37.2h23.1v-9.9h-23.1V1h-11v90.6c.1 4.9.9 10.2 3.5 14.2 4.7 7.5 13.7 8.9 20.4 8.9h19.9v-9.9h-18.5zM219.3 1v26.2h-23.1c-14 0-22.5 4.2-27.8 9.3-8.1 7.9-8.1 19.2-8.1 20.4v28.2c0 1.2 0 12.5 8.1 20.4 5.2 5.1 13.7 9.3 27.8 9.3h10.3c6.7 0 15.7-1.5 20.4-8.9 2.5-4 3.4-9.3 3.5-14.2V1h-11.1zM216 101.7c-2.2 2.1-5.8 3.2-11 3.2h-10c-9.1 0-14.8-2.6-18.2-6-4.1-4-5.5-9.3-5.5-13.4V56.6c0-4.1 1.4-9.4 5.5-13.4 3.5-3.4 9.1-6 18.2-6h24.2v53.9c.1 4.9-1 8.4-3.2 10.6zm462.2-58.5c3.5-3.4 9.1-6 18.2-6h26.5v-9.9h-25.4c-14 0-22.5 4.2-27.8 9.3-8.1 7.9-8.1 19.2-8.1 20.4v28.2c0 1.2 0 12.5 8.1 20.4 5.2 5.1 13.7 9.3 27.8 9.3h25.4V105h-26.5c-9.1 0-14.8-2.6-18.2-6-4.1-4-5.5-9.3-5.5-13.4v-29c0-4.2 1.4-9.5 5.5-13.4zM470.9 56.9c0-1.2 0-12.5-8.1-20.4-5.2-5.1-13.7-9.3-27.8-9.3h-24.5v9.9h25.6c9.1 0 14.8 2.6 18.2 6 4.1 4 5.5 9.3 5.5 13.4V65h-35.1c-6.7 0-15.7 1.5-20.4 8.9-2.5 4-3.4 9.3-3.5 14.2v3.5c.1 4.9.9 10.2 3.5 14.2 4.7 7.5 13.7 8.9 20.4 8.9H447c6.7 0 15.7-1.5 20.4-8.9 2.5-4 3.4-9.3 3.5-14.2V56.9zm-14.3 44.8c-2.2 2.1-5.8 3.2-11 3.2h-19.4c-5.2 0-8.8-1-11-3.2-2.2-2.2-3.2-5.7-3.2-10.6v-2.4c0-5 1.1-8.5 3.3-10.6 2.2-2.1 5.8-3.2 11-3.2h33.6v16.2c0 4.9-1.1 8.4-3.3 10.6zm196.3-44.8c0-1.2 0-12.5-8.1-20.4-5.2-5.1-13.7-9.3-27.8-9.3h-24.5v9.9h25.6c9.1 0 14.8 2.6 18.2 6 4.1 4 5.5 9.3 5.5 13.4V65h-35.1c-6.7 0-15.7 1.5-20.4 8.9-2.5 4-3.4 9.3-3.5 14.2v3.5c.1 4.9.9 10.2 3.5 14.2 4.7 7.5 13.7 8.9 20.4 8.9H629c6.7 0 15.7-1.5 20.4-8.9 2.5-4 3.4-9.3 3.5-14.2V56.9zm-14.3 44.8c-2.2 2.1-5.8 3.2-11 3.2h-19.4c-5.2 0-8.8-1-11-3.2-2.2-2.2-3.2-5.7-3.2-10.6v-2.4c0-5 1.1-8.5 3.3-10.6 2.2-2.1 5.8-3.2 11-3.2h33.6v16.2c0 4.9-1.1 8.4-3.3 10.6zM317.8 27.2h-11.5l-27.9 72.6-27.9-72.6h-11.4l33.6 87.5-10.1 26.3h11.5zm74.4 29.7c0-1.2 0-12.5-8-20.4-5.1-5-13.2-9.1-26.4-9.3h-1.2c-13.2.2-21.3 4.3-26.4 9.3-8 7.9-8 19.2-8 20.4v57.9h11V56.6c0-4.1 1.3-9.4 5.4-13.4 3.4-3.3 9.9-5.9 18.6-6 8.7.1 15.2 2.7 18.6 6 4 4 5.4 9.3 5.4 13.4v58.2h11V56.9zM791 36.5c-5.1-5-13.2-9.1-26.4-9.3h-1.2c-13.2.2-21.3 4.3-26.4 9.3-8 7.9-8 19.2-8 20.4v28.2c0 1.2 0 12.5 8 20.4 5.1 5 13.2 9.1 26.4 9.3h26v-10H764c-8.7-.1-15.2-2.7-18.6-6-4-4-5.4-9.3-5.4-13.4V75.1h59V56.9c0-1.2.1-12.5-8-20.4zm-50.9 28.7v-8.6c0-4.1 1.3-9.4 5.4-13.4 3.4-3.3 9.9-5.9 18.6-6 8.7.1 15.2 2.7 18.6 6 4 4 5.4 9.3 5.4 13.4v8.6h-48z"/>
              <g class="nav__logo__box">
                <path fill="#1496FF" d="M47.7 12.7c-1.8 9.5-4 23.6-5.2 37.9-2.1 25.2-.8 42.1-.8 42.1L6.2 126.4s-2.7-18.9-4.1-40.2C1.3 73 1 61.4 1 54.4c0-.4.2-.8.2-1.2 0-.5.6-5.2 5.2-9.6 5-4.8 41.9-33.7 41.3-30.9z"/>
                <path fill="#1284EA" d="M47.7 12.7c-1.8 9.5-4 23.6-5.2 37.9 0 0-39.3-4.7-41.5 4.8 0-.5.7-6.3 5.3-10.7 5-4.8 42-34.8 41.4-32z"/>
                <path fill="#B4DC00" d="M1 53.1v2.2c.4-1.7 1.1-2.9 2.5-4.8 2.9-3.7 7.6-4.7 9.5-4.9 9.6-1.3 23.8-2.8 38.1-3.2 25.3-.8 42 1.3 42 1.3L128.6 10S110 6.5 88.8 4c-13.9-1.7-26.1-2.6-33-3-.5 0-5.4-.6-10 3.8-5 4.8-30.4 28.9-40.6 38.6C.6 47.8 1 52.7 1 53.1z"/>
                <path fill="#6F2DA8" d="M127.3 96.2c-9.6 1.3-23.8 2.9-38.1 3.4-25.3.8-42.1-1.3-42.1-1.3l-35.5 33.8s18.8 3.7 40 6.1c13 1.5 24.5 2.3 31.5 2.7.5 0 1.3-.4 1.8-.4s5.4-.9 10-5.3c5-4.8 35.2-39.3 32.4-39z"/>
                <path fill="#591F91" d="M127.3 96.2c-9.6 1.3-23.8 2.9-38.1 3.4 0 0 2.7 39.5-6.8 41.2.5 0 7-.3 11.6-4.7 5-4.8 36.1-40.2 33.3-39.9z"/>
                <path fill="#73BE28" d="M84.5 141c-.7 0-1.4-.1-2.2-.1 1.8-.3 3-.9 4.9-2.3 3.8-2.7 5-7.4 5.4-9.3 1.7-9.5 4-23.6 5.1-37.9 2-25.2.8-42 .8-42L134 15.6s2.6 18.8 4.1 40.1c.9 13.9 1.2 26.2 1.3 33 0 .5.4 5.4-4.2 9.8-5 4.8-30.4 29-40.5 38.7-4.8 4.4-9.7 3.8-10.2 3.8z"/>
              </g>
          </svg>
        </a>
      </div>
      <div class="nav__buttongroup">
        <a class="nav__btn nav__btn--cta" href="https://www.dynatrace.com/trial/">
          Free trial
        </a>
      </div>
    </div>
     
        <ul class="breadcrumbs">
            <li class="breadcrumbs__item">
                <a class="breadcrumbs__link" href="/support/help/">Home</a>
            </li>
            <li class="breadcrumbs__item">
                <a class="breadcrumbs__link" href="/support/help/dynatrace-api/">Dynatrace API</a>
            </li>
            <li class="breadcrumbs__item">
                <a class="breadcrumbs__link" href="/support/help/dynatrace-api/environment-api/">Environment API</a>
            </li>
            <li class="breadcrumbs__item">
                <a class="breadcrumbs__link" href="/support/help/dynatrace-api/environment-api/metric-v2/">Metrics v2</a>
            </li>
            <li class="breadcrumbs__item">
                <span class="breadcrumbs__last">GET metrics</span>
            </li>
        </ul>
    <form action="https://search.dynatrace.com/?f=Category%5B%22Support%22%5D*&amp;f=Asset%20Type%5B%22Documentation%22%5D*&amp;f=Offering%5B%22Dynatrace%22%5D*" data-results="https://search.dynatrace.com/twigkit/api/core/services/platform/search/platforms.fusion.quickLinks?f=Category%5B%22Support%22%5D*&amp;f=Offering%5B%22Dynatrace%22%5D*&amp;f=Asset%20Type%5B%22Documentation%22%5D*" data-maxresults="5" method="GET" id="search" autocomplete="off" class="searchbar searchbar--top js-search">
      <input id="search-input" aria-label="Enter search term" type="search" class="inputfield inputfield--search nav__search js-search-input" name="q" placeholder="Search Dynatrace Help">
      <input type="hidden" name="f" value="Category[&quot;Support&quot;]*">
      <input type="hidden" name="f" value="Asset Type[&quot;Documentation&quot;]*">
      <input type="hidden" name="f" value="Offering[&quot;Dynatrace&quot;]*">
    </form>
    <a aria-label="Search" href="https://search.dynatrace.com/?f=Category%5B%22Support%22%5D*&amp;f=Asset%20Type%5B%22Documentation%22%5D*&amp;f=Offering%5B%22Dynatrace%22%5D*" class="nav__search__icon js-nav-search-icon"></a>
    
    <div class="layout is-flex">
      <nav class="sidebar">
        <form action="https://search.dynatrace.com/?f=Category%5B%22Support%22%5D*&amp;f=Asset%20Type%5B%22Documentation%22%5D*&amp;f=Offering%5B%22Dynatrace%22%5D*" data-results="https://search.dynatrace.com/twigkit/api/core/services/platform/search/platforms.fusion.quickLinks?f=Category%5B%22Support%22%5D*&amp;f=Offering%5B%22Dynatrace%22%5D*&amp;f=Asset%20Type%5B%22Documentation%22%5D*" data-maxresults="5" method="GET" id="search" autocomplete="off" class="searchbar searchbar--sidebar js-search">
          <input id="search-input" aria-label="Enter search term" type="search" class="inputfield inputfield--search nav__search js-search-input" name="q" placeholder="Search Dynatrace Help">
          <input type="hidden" name="f" value="Category[&quot;Support&quot;]*">
          <input type="hidden" name="f" value="Asset Type[&quot;Documentation&quot;]*">
          <input type="hidden" name="f" value="Offering[&quot;Dynatrace&quot;]*">
        </form>
        <a aria-label="Search" href="https://search.dynatrace.com/?f=Category%5B%22Support%22%5D*&amp;f=Asset%20Type%5B%22Documentation%22%5D*&amp;f=Offering%5B%22Dynatrace%22%5D*" class="nav__search__icon js-nav-search-icon"></a>
      
        <ul class="toc__menu" role="tree" tabindex="0"><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Get started
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/get-started/what-is-dynatrace/" tabindex="-1">
      
          What is Dynatrace?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/get-started/get-started-with-dynatrace-saas/" tabindex="-1">
      
          Get started with Dynatrace SaaS
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/get-started/get-started-with-dynatrace-managed/" tabindex="-1">
      
          Get started with Dynatrace Managed
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          What&apos;s new
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/whats-new/release-notes/" tabindex="-1">
      
          Release notes
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          SaaS
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-197/" tabindex="-1">
      
          Version 1.197
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-196/" tabindex="-1">
      
          Version 1.196
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-195/" tabindex="-1">
      
          Version 1.195
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-194/" tabindex="-1">
      
          Version 1.194
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-193/" tabindex="-1">
      
          Version 1.193
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-192/" tabindex="-1">
      
          Version 1.192
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-191/" tabindex="-1">
      
          Version 1.191
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-190/" tabindex="-1">
      
          Version 1.190
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-189/" tabindex="-1">
      
          Version 1.189
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-188/" tabindex="-1">
      
          Version 1.188
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/saas/sprint-187/" tabindex="-1">
      
          Version 1.187
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Managed
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/managed/sprint-196/" tabindex="-1">
      
          Version 1.196
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/managed/sprint-194/" tabindex="-1">
      
          Version 1.194
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/managed/sprint-192/" tabindex="-1">
      
          Version 1.192
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/managed/sprint-190/" tabindex="-1">
      
          Version 1.190
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/managed/sprint-188/" tabindex="-1">
      
          Version 1.188
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/managed/sprint-186/" tabindex="-1">
      
          Version 1.186
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          OneAgent
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/oneagent/sprint-195/" tabindex="-1">
      
          Version 1.195
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/oneagent/sprint-193/" tabindex="-1">
      
          Version 1.193
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/oneagent/sprint-191/" tabindex="-1">
      
          Version 1.191
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/oneagent/sprint-189/" tabindex="-1">
      
          Version 1.189
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/oneagent/sprint-187/" tabindex="-1">
      
          Version 1.187
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/oneagent/sprint-185/" tabindex="-1">
      
          Version 1.185
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          ActiveGate
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/activegate/sprint-195/" tabindex="-1">
      
          Version 1.195
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/activegate/sprint-193/" tabindex="-1">
      
          Version 1.193
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/activegate/sprint-191/" tabindex="-1">
      
          Version 1.191
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/activegate/sprint-189/" tabindex="-1">
      
          Version 1.189
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/activegate/sprint-187/" tabindex="-1">
      
          Version 1.187
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/activegate/sprint-185/" tabindex="-1">
      
          Version 1.185
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Dynatrace API
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-197/" tabindex="-1">
      
          Version 1.197
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-196/" tabindex="-1">
      
          Version 1.196
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-195/" tabindex="-1">
      
          Version 1.195
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-194/" tabindex="-1">
      
          Version 1.194
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-193/" tabindex="-1">
      
          Version 1.193
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-192/" tabindex="-1">
      
          Version 1.192
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-191/" tabindex="-1">
      
          Version 1.191
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-190/" tabindex="-1">
      
          Version 1.190
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-189/" tabindex="-1">
      
          Version 1.189
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-188/" tabindex="-1">
      
          Version 1.188
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/sprint-187/" tabindex="-1">
      
          Version 1.187
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/dynatrace-api/deprecated-apis/" tabindex="-1">
      
          Deprecated APIs
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Davis Assistant
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/davis-assistant/sprint-194/" tabindex="-1">
      
          Version 1.194
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/davis-assistant/sprint-190/" tabindex="-1">
      
          Version 1.190
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/davis-assistant/sprint-186/" tabindex="-1">
      
          Version 1.186
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/davis-assistant/sprint-184/" tabindex="-1">
      
          Version 1.184
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/zos-code-module-changelog/" tabindex="-1">
      
          z/OS code modules changelog for 7.2 release
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/release-notes/previous-releases/" tabindex="-1">
      
          Previous releases
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="https://www.dynatrace.com/news/category/product-news/" tabindex="-1">
      
          Product news
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/new-help-topics/" tabindex="-1">
      
          New Help topics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/preview-and-early-adopter-releases/" tabindex="-1">
      
          Previews and Early Adopter releases
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/whats-new/end-of-support-news/" tabindex="-1">
      
          End-of-support news
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Technology support
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Cloud platforms
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/" tabindex="-1">
      
          Amazon Web Services
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/aws-monitoring-with-dynatrace-saas/" tabindex="-1">
      
          Set up Dynatrace SaaS for AWS monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/aws-monitoring-with-dynatrace-managed/" tabindex="-1">
      
          Set up Dynatrace Managed for AWS monitoring
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Integrations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/deploy-oneagent-on-aws-fargate/" tabindex="-1">
      
          Deploy OneAgent on AWS Fargate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/deploy-oneagent-on-ecs/" tabindex="-1">
      
          Deploy OneAgent on Elastic Container Service (EC2)
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/deploy-oneagent-using-aws-elastic-beanstalk/" tabindex="-1">
      
          Deploy OneAgent on AWS Elastic Beanstalk
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/elastic-kubernetes-service/" tabindex="-1">
      
          Elastic Kubernetes Service
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/integrate-nodejs-lambda-functions/" tabindex="-1">
      
          Serverless Lambda function integration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/configuration/cors-in-amazon-s3/" tabindex="-1">
      
          CORS Amazon S3
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/configuration/connect-to-dynatrace-using-aws-privatelink/" tabindex="-1">
      
          Connect to Dynatrace using AWS PrivateLink
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/configuration/define-hosts-naming-rule-based-on-aws-tags/" tabindex="-1">
      
          Define host naming rules based on AWS tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/configuration/limit-api-calls-to-aws-using-tags/" tabindex="-1">
      
          Limit API calls to AWS using tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/configuration/aws-supporting-services/" tabindex="-1">
      
          Monitoring additional AWS services
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/view-aws-monitoring-results/" tabindex="-1">
      
          Monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/amazon-web-services/troubleshoot-aws-monitoring-setup/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/" tabindex="-1">
      
          Microsoft Azure
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Azure Services
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/" tabindex="-1">
      
          Service monitoring
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-batch/" tabindex="-1">
      
          Azure Batch
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-db-mariadb/" tabindex="-1">
      
          Azure Database for MariaDB
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-db-mysql/" tabindex="-1">
      
          Azure Database for MySQL
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-db-postgresql/" tabindex="-1">
      
          Azure Database for PostgreSQL
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-front-door/" tabindex="-1">
      
          Azure Front Door
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-hdinsight/" tabindex="-1">
      
          Azure HDInsight
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-sql-managed-instance/" tabindex="-1">
      
          Azure SQL Managed Instance
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-traffic-manager/" tabindex="-1">
      
          Azure Traffic Manager
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-virtual-machines/" tabindex="-1">
      
          Azure Virtual Machines (classic)
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-virtual-network-gateways/" tabindex="-1">
      
          Azure Virtual Network Gateway
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machines/" tabindex="-1">
      
          Virtual Machines
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machines/deploy-oneagent-on-azure-virtual-machines/" tabindex="-1">
      
          Deploy OneAgent on Azure Virtual Machines
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machine-scale-sets/" tabindex="-1">
      
          Virtual Machine Scale Sets
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machine-scale-sets/deploy-oneagent-on-azure-vm-scaleset/" tabindex="-1">
      
          Deploy OneAgent on Azure Virtual Machine Scale Set
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machine-scale-sets/troubleshoot-oneagent-deployment-on-azure-vm-scaleset/" tabindex="-1">
      
          Troubleshoot OneAgent deployment on Azure VM Scale Set
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-functions/" tabindex="-1">
      
          Azure Functions
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-functions/deploy-oneagent-on-azure-functions/" tabindex="-1">
      
          Deploy OneAgent on Azure Functions
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-monitor/" tabindex="-1">
      
          Azure Monitor
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-monitor/set-up-integration-for-azure-alerts/" tabindex="-1">
      
          Set up integration for Azure Alerts
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-monitor/set-up-integration-with-azure-monitor/" tabindex="-1">
      
          Set up integration with Azure Monitor
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/" tabindex="-1">
      
          App Service
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/deploy-oneagent-on-azure-app-service/" tabindex="-1">
      
          Deploy OneAgent on Azure App Service
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/update-oneagent-on-azure-app-service/" tabindex="-1">
      
          Update OneAgent on Azure App Service
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/troubleshoot-oneagent-deployment-on-azure-app-service/" tabindex="-1">
      
          Troubleshoot OneAgent deployment on Azure App Service
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/uninstall-oneagent-from-azure-app-service/" tabindex="-1">
      
          Uninstall OneAgent from Azure App Service
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-fabric/" tabindex="-1">
      
          Service Fabric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-kubernetes-service/" tabindex="-1">
      
          Azure Kubernetes Service
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/" tabindex="-1">
      
          Cloud Foundry
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry/" tabindex="-1">
      
          Deploy OneAgent BOSH release
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/monitoring/connect-your-cloud-foundry-foundations-to-dynatrace/" tabindex="-1">
      
          Monitor your clusters with Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/monitoring/cloud-foundry-metrics/" tabindex="-1">
      
          Cloud Foundry metrics overview
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Maintenance
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/update-oneagent-on-cloud-foundry/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/uninstall-oneagent-from-cloud-foundry/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/dynatrace-support-model-for-pivotal-platform/" tabindex="-1">
      
          Support lifecycle
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/troubleshoot/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Other deployments and configurations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deployment-strategies/" tabindex="-1">
      
          Deployment strategies
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deploy-oneagent-on-ibm-cloud-foundry-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent on IBM Cloud Foundry
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deploy-oneagent-on-pivotal-web-services-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent on Pivotal Web Services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent on SAP Cloud Platform
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/install-the-service-broker-for-cloud-foundry-dashboard-tile/" tabindex="-1">
      
          Install Dynatrace Service Broker
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/leverage-tags-defined-in-cloud-foundry-deployments/" tabindex="-1">
      
          Organize Cloud Foundry deployments by tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/define-process-group-metadata-for-cloud-foundry-applications/" tabindex="-1">
      
          Process group metadata for Cloud Foundry
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/" tabindex="-1">
      
          Google Cloud Platform
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/deploy-oneagent-for-google-app-engine-apps/" tabindex="-1">
      
          OneAgent on Google App Engine
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/google-kubernetes-engine/" tabindex="-1">
      
          OneAgent on Google Kubernetes Engine
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/google-compute-engine/" tabindex="-1">
      
          OneAgent on Google Compute Engine
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/" tabindex="-1">
      
          Kubernetes
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/deploy-oneagent-k8/" tabindex="-1">
      
          Deploy OneAgent Operator
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/monitoring/monitor-kubernetes-clusters-with-dynatrace/" tabindex="-1">
      
          Monitor your clusters with Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/monitoring/monitor-kubernetes-openshift-clusters/" tabindex="-1">
      
          Cluster utilization
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/monitoring/events/" tabindex="-1">
      
          Events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/monitoring/monitor-workloads-kubernetes/" tabindex="-1">
      
          Workloads
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Maintenance
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/maintenance/update-oneagent-on-kubernetes/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/maintenance/uninstall-oneagent-from-kubernetes/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/maintenance/migrate-tenant-k8/" tabindex="-1">
      
          Migrate OneAgent Operator to a new Dynatrace Kubernetes tenant
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/maintenance/support-model-for-kubernetes/" tabindex="-1">
      
          Support lifecycle
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/maintenance/troubleshoot-deployment-and-connectivity/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Other deployments and configurations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/other-deployments-and-configurations/kubernetes-deployment-strategies/" tabindex="-1">
      
          Deployment strategies
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/other-deployments-and-configurations/deploy-daemonset/" tabindex="-1">
      
          Deploy OneAgent Daemonset
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/other-deployments-and-configurations/deploy-oneagent-on-kubernetes-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent for application-only monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/other-deployments-and-configurations/oneagent-in-air-gapped-kubernetes-environment/" tabindex="-1">
      
          Prerequisites for air-gapped clusters
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/other-deployments-and-configurations/leverage-tags-defined-in-kubernetes-deployments/" tabindex="-1">
      
          Organize Kubernetes deployments by tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/other-deployments-and-configurations/configure-istio-for-oneagent-traffic-in-kubernetes/" tabindex="-1">
      
          Configure Istio
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/openshift/" tabindex="-1">
      
          Red Hat OpenShift
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/deploy-oneagent-openshift/" tabindex="-1">
      
          Deploy OneAgent Operator
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/monitor-openshift-clusters-with-dynatrace/" tabindex="-1">
      
          Monitor your clusters with Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/monitor-openshift-cluster-utilization/" tabindex="-1">
      
          Cluster utilization
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/events/" tabindex="-1">
      
          Events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/monitor-workloads-openshift/" tabindex="-1">
      
          Workloads
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Maintenance
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/update-oneagent-on-openshift/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/uninstall-oneagent-from-openshift/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/migrate-tenant-openshift/" tabindex="-1">
      
          Migrate OneAgent Operator to a new Dynatrace OpenShift tenant
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/dynatrace-support-model-for-openshift/" tabindex="-1">
      
          Support lifecycle
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/troubleshoot-oneagent-on-openshift/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Other deployments and configurations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/openshift-deployment-strategies/" tabindex="-1">
      
          Deployment strategies
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/deploy-daemonset/" tabindex="-1">
      
          Deploy OneAgent Daemonset
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/deploy-oneagent-on-openshift-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent for application-only monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/deploy-with-operatorhub/" tabindex="-1">
      
          Deploy OneAgent via OperatorHub
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/oneagent-in-airgapped-openshift-environment/" tabindex="-1">
      
          Prerequisites for air-gapped clusters
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/leverage-tags-defined-in-openshift-deployments/" tabindex="-1">
      
          Organize OpenShift deployments by tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/configure-istio-for-oneagent-traffic-in-openshift/" tabindex="-1">
      
          Configure Istio
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Other platforms
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/docker/" tabindex="-1">
      
          Docker
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/docker/basic-concepts/how-dynatrace-monitors-containers/" tabindex="-1">
      
          How Dynatrace monitors containers
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/docker/monitoring/monitor-docker-containers/" tabindex="-1">
      
          Monitor Docker containers
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/docker/installation-and-operation/" tabindex="-1">
      
          Installation and operation
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/docker/installation-and-operation/deploy-dynatrace-oneagent-as-docker-container/" tabindex="-1">
      
          Deploy Dynatrace OneAgent as a Docker container
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/docker/installation-and-operation/update-oneagent-on-docker-containers/" tabindex="-1">
      
          Update OneAgent on Docker containers
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/" tabindex="-1">
      
          Heroku
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation and operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/installation-and-operation/deploy-oneagent-on-heroku/" tabindex="-1">
      
          Deploy OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/installation-and-operation/update-oneagent-on-heroku/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/monitoring/monitor-your-heroku-applications/" tabindex="-1">
      
          Monitor your Heroku applications
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/mesos-marathon/" tabindex="-1">
      
          Mesos/Marathon
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/mesos-marathon/deploy-dynatrace-oneagent-on-mesos-marathon/" tabindex="-1">
      
          Deploy OneAgent on Mesos/Marathon
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Virtualization
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/virtualization/vmware/" tabindex="-1">
      
          VMware
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/virtualization/vmware/set-up-virtualization-monitoring/" tabindex="-1">
      
          Set up virtualization monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/virtualization/vmware/where-to-view-virtualization-monitoring-data/" tabindex="-1">
      
          View virtualization monitoring data
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/virtualization/vmware/measurements-for-esxi-host-health/" tabindex="-1">
      
          Measurements for ESXi host health
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/virtualization/vmware/how-does-virtual-machine-migration-affect-performance/" tabindex="-1">
      
          Virtual machine migration and performance
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operating systems
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/linux/" tabindex="-1">
      
          Linux
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux/" tabindex="-1">
      
          Disk space requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/permission-requirements-for-oneagent-installation-and-operation-on-linux/" tabindex="-1">
      
          Permission requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/install-oneagent-on-linux/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/install-oneagent-on-ppc-be-linux/" tabindex="-1">
      
          Install OneAgent on PPC BE Linux
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/customize-oneagent-installation-on-linux/" tabindex="-1">
      
          Customize installation
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-linux/" tabindex="-1">
      
          How to pass a proxy address
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/oneagent-files-and-logs-on-linux/" tabindex="-1">
      
          OneAgent files and logs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/update-oneagent-on-linux/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/update-oneagent-on-ppc-be-linux/" tabindex="-1">
      
          Update OneAgent on PPC BE Linux
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/stop-restart-oneagent-on-linux/" tabindex="-1">
      
          Stop/restart OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/uninstall-oneagent-on-linux/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Related topics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/related-topics/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor/" tabindex="-1">
      
          How to enable deep monitoring for applications confined by AppArmor
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-configuration-via-command-line-interface/" tabindex="-1">
      
          OneAgent configuration via command-line interface
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/windows/" tabindex="-1">
      
          Windows
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows/" tabindex="-1">
      
          Disk space requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/permission-requirements-for-oneagent-installation-and-operation-on-windows/" tabindex="-1">
      
          Permission requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/install-oneagent-on-windows/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/customize-oneagent-installation-on-windows/" tabindex="-1">
      
          Customize installation
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows/" tabindex="-1">
      
          How to pass a proxy address
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/oneagent-files-and-logs-on-windows/" tabindex="-1">
      
          OneAgent files and logs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/update-oneagent-on-windows/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/stop-restart-oneagent-on-windows/" tabindex="-1">
      
          Stop/restart OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/uninstall-oneagent-on-windows/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Related topics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-configuration-via-command-line-interface/" tabindex="-1">
      
          OneAgent configuration via command-line interface
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/ios/" tabindex="-1">
      
          iOS
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/instrumentation/get-started-with-ios-monitoring/" tabindex="-1">
      
          Get started with iOS monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/instrumentation/dynatrace-auto-instrumentation-for-ios/" tabindex="-1">
      
          Dynatrace auto-instrumentation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Customization
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/configuration-settings/" tabindex="-1">
      
          Configuration settings
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/oneagent-sdk-for-ios/" tabindex="-1">
      
          OneAgent SDK for iOS
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/logging-for-ios/" tabindex="-1">
      
          Logging
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/android/" tabindex="-1">
      
          Android
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation via plugin
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/android-gradle-plugin/" tabindex="-1">
      
          Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/instrumentation-via-plugin/" tabindex="-1">
      
          Instrumentation via Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/monitoring-capabilities/" tabindex="-1">
      
          Monitoring capabilities of Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/configure-plugin-for-instrumentation/" tabindex="-1">
      
          Configure Dynatrace Android Gradle plugin for instrumentation processes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/adjust-oneagent-configuration/" tabindex="-1">
      
          Use Dynatrace Android Gradle plugin to adjust OneAgent configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/configure-multi-module-projects/" tabindex="-1">
      
          Configure multi-module Android projects with Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation via OneAgent sdk
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android/" tabindex="-1">
      
          OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/adjust-oneagent-communication/" tabindex="-1">
      
          Adjust communication with OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/manual-instrumentation/" tabindex="-1">
      
          Standalone manual instrumentation using OneAgent SDK for Android
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/troubleshooting/faqs/" tabindex="-1">
      
          Dynatrace Android Gradle plugin FAQs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/troubleshooting/debug-logging-oneagent/" tabindex="-1">
      
          Debug logging for OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Legacy documentation
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Customization
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/oneagent-sdk-for-android/" tabindex="-1">
      
          OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/advanced-settings-for-android-auto-instrumentation/" tabindex="-1">
      
          Advanced settings
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/auto-instrumentation-properties-for-multidex-apps/" tabindex="-1">
      
          Auto-instrumentation properties for multidex apps
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/logging-for-android/" tabindex="-1">
      
          Logging
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/get-started-with-android-monitoring/" tabindex="-1">
      
          Get started with Android monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/dynatrace-auto-instrumentation-for-android/" tabindex="-1">
      
          Dynatrace auto-instrumentation
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/dynatrace-gradle-plugin-for-android-app-auto-instrumentation/" tabindex="-1">
      
          Dynatrace Gradle plugin
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/manual-instrumentation-for-android/" tabindex="-1">
      
          Manual instrumentation
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/command-line-auto-instrumentation-for-android/" tabindex="-1">
      
          Command-line auto-instrumentation for Android
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/troubleshoot-oneagent-auto-instrumentation-on-android/" tabindex="-1">
      
          Instrumentation
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/migration/" tabindex="-1">
      
          Migration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/troubleshoot-monitoring-of-mobile-apps-on-android/" tabindex="-1">
      
          Monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/aix/" tabindex="-1">
      
          AIX
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix/" tabindex="-1">
      
          Disk space requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/install-oneagent-on-aix/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/permission-requirements-for-oneagent-installation-and-operation-on-aix/" tabindex="-1">
      
          Permission requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/customize-oneagent-installation-on-aix/" tabindex="-1">
      
          Customize installation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/enable-auto-injection/" tabindex="-1">
      
          Auto-injection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/update-oneagent-on-aix/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/stop-restart-oneagent-on-aix/" tabindex="-1">
      
          Stop/restart OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/uninstall-oneagent-on-aix/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Related topics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-configuration-via-command-line-interface/" tabindex="-1">
      
          OneAgent configuration via command-line interface
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/solaris/" tabindex="-1">
      
          Solaris
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/solaris/installation/install-oneagent-on-solaris/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/solaris/operation/update-oneagent-on-solaris/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/solaris/operation/troubleshoot-oneagent-installation-on-solaris/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/zos/" tabindex="-1">
      
          z/OS
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/zos-deployment-overview/" tabindex="-1">
      
          Installation overview
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/download-oneagent-zos/" tabindex="-1">
      
          Download OneAgent to z/OS
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/zos/installation/install-zdc/" tabindex="-1">
      
          Install the zDC
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/install-zdc/install-multiple-zdc-zremote/" tabindex="-1">
      
          Install multiple instances of zDC/zRemote
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/install-oneagent-cics/" tabindex="-1">
      
          Install OneAgent on CICS
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/install-oneagent-ims/" tabindex="-1">
      
          Install OneAgent on IMS
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/install-oneagent-ctg-ims-soap/" tabindex="-1">
      
          Install OneAgent on CTG and IMS SOAP gateway
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/install-zremote/" tabindex="-1">
      
          Install the zRemote
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/verify-the-installation/" tabindex="-1">
      
          Verify the installation
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/installation/troubleshoot-oneagent-installation-on-zos/" tabindex="-1">
      
          Troubleshooting
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/cics-ims-mq-monitoring/" tabindex="-1">
      
          CICS, IMS and MQ monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/cics-and-ims-sdk/" tabindex="-1">
      
          CICS and IMS SDK
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/zdc-reference-info/" tabindex="-1">
      
          zDC reference
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/dtax-transaction/" tabindex="-1">
      
          DTAX transaction
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/zos-code-module-logs/" tabindex="-1">
      
          z/OS code module logs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/zos-code-module-messages/" tabindex="-1">
      
          z/OS code module messages
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/cics-backtrace-purepath/" tabindex="-1">
      
          CICS backtrace and PurePath
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/zos/operation/ibm-z-infrastructure-metrics/" tabindex="-1">
      
          IBM Z infrastructure metrics
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Application software
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/application-software/java/" tabindex="-1">
      
          Java
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Support
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/java/support/support-for-jvms/" tabindex="-1">
      
          Support for JVMs
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/java/concepts/g1-garbage-collector-java-9/" tabindex="-1">
      
          G1 Garbage Collector &#x2013; Java 9
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/java/concepts/top-java-memory-problems/" tabindex="-1">
      
          Top Java memory problems
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration and analysis
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/java/configuration-and-analysis/identify-memory-leaks/" tabindex="-1">
      
          Identify memory leaks
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/java/configuration-and-analysis/define-custom-java-services/" tabindex="-1">
      
          Define custom Java services
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/dotnet/" tabindex="-1">
      
          .NET
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/nodejs/" tabindex="-1">
      
          Node.js
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/application-software/php/" tabindex="-1">
      
          PHP
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/php/monitoring/code-level-visibility/" tabindex="-1">
      
          Code-level visibility for PHP
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/php/monitoring/custom-service-detection/" tabindex="-1">
      
          Custom service detection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/php/monitoring/full-stack-monitoring/" tabindex="-1">
      
          Full-stack PHP monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/php/monitoring/php-fpm/" tabindex="-1">
      
          PHP-FPM monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Support
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/php/support/supported-versions/" tabindex="-1">
      
          Supported PHP versions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/php/support/known-limitations/" tabindex="-1">
      
          Known limitations for PHP support
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/go/" tabindex="-1">
      
          Go
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/nginx/" tabindex="-1">
      
          NGINX
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/application-software/other-technologies/" tabindex="-1">
      
          Other technologies
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Supported out of the box
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/activemq/" tabindex="-1">
      
          ActiveMQ
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/apache-cordova/" tabindex="-1">
      
          Apache Cordova
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/cassandra/" tabindex="-1">
      
          Cassandra
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/couchbase/" tabindex="-1">
      
          Couchbase
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/couchdb/" tabindex="-1">
      
          CouchDB
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/elasticsearch/" tabindex="-1">
      
          Elasticsearch
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/hadoop/" tabindex="-1">
      
          Hadoop
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/haproxy/" tabindex="-1">
      
          HAProxy
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/ibm-mq/" tabindex="-1">
      
          IBM MQ
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/kafka/" tabindex="-1">
      
          Kafka
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/memcached/" tabindex="-1">
      
          Memcached
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/microsoft-sql-server/" tabindex="-1">
      
          Microsoft SQL Server
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/php-fpm/" tabindex="-1">
      
          PHP-FPM
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/postgresql/" tabindex="-1">
      
          PostgreSQL
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/rabbitmq/" tabindex="-1">
      
          RabbitMQ
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/react-native/" tabindex="-1">
      
          React Native
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/redis/" tabindex="-1">
      
          Redis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/spark/" tabindex="-1">
      
          Spark
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/varnish-cache/" tabindex="-1">
      
          Varnish Cache
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/xamarin/" tabindex="-1">
      
          Xamarin
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Dynatrace extension required
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/datapower/" tabindex="-1">
      
          IBM DataPower
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/f5-big-ip-ltm/" tabindex="-1">
      
          F5 BIG-IP LTM
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/windows-server-2003/" tabindex="-1">
      
          Windows Server
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/apigee-edge/" tabindex="-1">
      
          Apigee Edge
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/citrix-netscaler/" tabindex="-1">
      
          Citrix NetScaler
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/citrix-xenapp-xendesktop/" tabindex="-1">
      
          Citrix Virtual Apps and Desktops
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/ibm-iseries-as400/" tabindex="-1">
      
          IBM i (formerly known as IBM iSeries or IBM AS400)
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/juniper-networks-junosos/" tabindex="-1">
      
          Juniper Networks
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/sap/" tabindex="-1">
      
          SAP ABAP platform
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/dynatrace-extension-required/tibco-ems/" tabindex="-1">
      
          Tibco EMS
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/supported-technologies-and-versions/" tabindex="-1">
      
          All supported technologies and versions
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-technology-support/oneagent-platform-and-capability-support-matrix/" tabindex="-1">
      
          OneAgent platform and capability support matrix
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Setup and configuration
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/dynatrace-managed/" tabindex="-1">
      
          Dynatrace Managed
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/basic-concepts/overview-of-dynatrace-managed/" tabindex="-1">
      
          Overview of Dynatrace Managed components
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/basic-concepts/dynatrace-managed-cluster-failover-mechanism/" tabindex="-1">
      
          Dynatrace Managed cluster failover mechanism
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/basic-concepts/dynatrace-managed-multi-data-center/" tabindex="-1">
      
          High availability for multi-data centers
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/managed-deployment-scenarios/" tabindex="-1">
      
          Managed deployment scenarios
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/dynatrace-managed-hardware-and-system-requirements/" tabindex="-1">
      
          Dynatrace Managed hardware and system requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/managed-hardware-requirements-for-clouds/" tabindex="-1">
      
          Managed hardware recommendations for cloud deployments
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/set-up-a-cluster/" tabindex="-1">
      
          Set up a cluster
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/add-a-new-cluster-node/" tabindex="-1">
      
          Add a new cluster node
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/customize-installation-for-dynatrace-managed/" tabindex="-1">
      
          Customize installation for Dynatrace Managed
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/how-to-install-a-cluster-activegate/" tabindex="-1">
      
          Install a Cluster ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/installation/install-your-own-ssl-certificate/" tabindex="-1">
      
          Install your own SSL certificate
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Users and groups setup
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/users-and-groups-setup/user-groups-and-permissions/" tabindex="-1">
      
          User groups and permissions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/users-and-groups-setup/manage-users-and-groups-with-ldap/" tabindex="-1">
      
          Manage users and groups via LDAP
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/users-and-groups-setup/manage-users-and-groups-with-saml/" tabindex="-1">
      
          Manage users and groups with SAML in Dynatrace Managed
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/users-and-groups-setup/manage-users-and-groups-with-openid/" tabindex="-1">
      
          Manage users and groups with OpenID in Dynatrace Managed
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Data privacy
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/data-privacy/data-exchange-between-a-managed-cluster-and-mission-control/" tabindex="-1">
      
          Data privacy and exchange in Managed deployments
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/data-privacy/monitored-technologies/" tabindex="-1">
      
          Monitored technologies and feature usage
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/data-privacy/how-does-mission-control-pro-active-support-work/" tabindex="-1">
      
          How does Mission Control pro-active support work?
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/configuration/configurable-properties-of-dynatrace-managed/" tabindex="-1">
      
          Configurable properties of Dynatrace Managed
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/configuration/which-network-ports-does-dynatrace-server-use/" tabindex="-1">
      
          Cluster node ports
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/configuration/how-to-add-a-certificate-to-server-trust-store/" tabindex="-1">
      
          How to add a certificate to Dynatrace Server TrustStore
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/configuration/can-i-use-a-proxy-for-internet-access/" tabindex="-1">
      
          Can I use a proxy for internet access?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/configuration/configure-smtp-server-connection/" tabindex="-1">
      
          Configure an SMTP server connection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/configuration/cluster-remote-access/" tabindex="-1">
      
          Cluster remote access
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/configuration/configure-manage-user-sessions/" tabindex="-1">
      
          Configure and manage user sessions
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/migrate-a-cluster/" tabindex="-1">
      
          Migrate a cluster
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/add-second-data-center/" tabindex="-1">
      
          Replicate nodes across DCs for Premium HA
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/manage-your-monitoring-environments/" tabindex="-1">
      
          Manage your monitoring environments
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/enable-disable-a-cluster-node/" tabindex="-1">
      
          Enable/Disable a cluster node
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/change-storage-location/" tabindex="-1">
      
          Change storage location
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/apply-operating-system-patches-to-a-node/" tabindex="-1">
      
          Apply operating system patches to a node
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/update-dynatrace-managed/" tabindex="-1">
      
          Update Dynatrace Managed
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/update-dynatrace-managed-activegate/" tabindex="-1">
      
          Update cluster ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/back-up-and-restore-a-cluster/" tabindex="-1">
      
          Back up and restore a cluster
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/estimating-cluster-backup-size/" tabindex="-1">
      
          Estimate cluster backup size
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/remove-a-cluster-node/" tabindex="-1">
      
          Remove a cluster node
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/remove-a-cluster/" tabindex="-1">
      
          Remove a cluster
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/diagnostic-archives-for-managed-installations/" tabindex="-1">
      
          Diagnostic archives for Managed installations
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/dynatrace-script/" tabindex="-1">
      
          Execute dynatrace.sh bash script
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/operation/troubleshoot-dynatrace-managed/" tabindex="-1">
      
          Troubleshoot Dynatrace Managed
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Cluster API
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/basics/cluster-api-authentication/" tabindex="-1">
      
          Cluster API - Authentication
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/basics/cluster-api-response-codes/" tabindex="-1">
      
          Response codes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/basics/cluster-access-limit/" tabindex="-1">
      
          Access limit
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/basics/cluster-preview-early-access/" tabindex="-1">
      
          Preview and Early Adopter releases
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/cluster-management-api/" tabindex="-1">
      
          Cluster Management API
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/" tabindex="-1">
      
          Dynatrace Cluster API
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Cluster tokens
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/cluster-tokens/list-cluster-tokens/" tabindex="-1">
      
          List available Cluster tokens
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/cluster-tokens/create-cluster-tokens/" tabindex="-1">
      
          Create new Cluster token
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/cluster-tokens/list-cluster-token-metadata-para/" tabindex="-1">
      
          List Cluster token metadata with id
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/cluster-tokens/update-cluster-token/" tabindex="-1">
      
          Update Cluster token
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/cluster-tokens/delete-cluster-token/" tabindex="-1">
      
          Delete Cluster token
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/cluster-tokens/list-cluster-token-metadata-req/" tabindex="-1">
      
          List Cluster token metadata with request
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Remote access
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/remote-access/get-all-cluster-access-requests/" tabindex="-1">
      
          Get all cluster access requests
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/remote-access/post-remote-access-permission/" tabindex="-1">
      
          Grant remote access permission
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/remote-access/get-cluster-access-request/" tabindex="-1">
      
          Get cluster access request
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/remote-access/put-change-access-request-state/" tabindex="-1">
      
          Change state of access request
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          User management
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/user-management/get-cluster-user-sessions-configuration/" tabindex="-1">
      
          Get cluster user sessions configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/user-management/update-cluster-user-sessions-configuration/" tabindex="-1">
      
          Update cluster user sessions configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/user-management/get-cluster-user-sessions/" tabindex="-1">
      
          Get cluster user sessions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/dynatrace-cluster-api/user-management/delete-cluster-user-session/" tabindex="-1">
      
          Delete user sessions of a given user
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/cluster-api/cluster-token-rotation-api/" tabindex="-1">
      
          Rotating cluster tokens via API
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/" tabindex="-1">
      
          Dynatrace OneAgent
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Requirements
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/requirements/memory-requirements/" tabindex="-1">
      
          OneAgent code module memory requirements
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          OneAgent technology support
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-technology-support/oneagent-platform-and-capability-support-matrix/" tabindex="-1">
      
          OneAgent platform and capability support matrix
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/supported-technologies-and-versions/" tabindex="-1">
      
          All supported technologies and versions
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-configuration-via-command-line-interface/" tabindex="-1">
      
          OneAgent configuration via command-line interface
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/troubleshooting/troubleshoot-oneagent-deep-monitoring-issues/" tabindex="-1">
      
          Troubleshoot OneAgent deep-monitoring issues
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/troubleshooting/troubleshoot-monitoring-interruptions/" tabindex="-1">
      
          Troubleshoot monitoring interruptions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/troubleshooting/troubleshoot-oneagent-installation/" tabindex="-1">
      
          Troubleshoot OneAgent installation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Capabilities
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/capabilities/supported-monitoring-types/" tabindex="-1">
      
          OneAgent monitoring capabilities
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/capabilities/how-one-agent-works/" tabindex="-1">
      
          How OneAgent works
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation and operation
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/aix/" tabindex="-1">
      
          AIX
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix/" tabindex="-1">
      
          Disk space requirements
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/install-oneagent-on-aix/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/permission-requirements-for-oneagent-installation-and-operation-on-aix/" tabindex="-1">
      
          Permission requirements
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/installation/customize-oneagent-installation-on-aix/" tabindex="-1">
      
          Customize installation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/enable-auto-injection/" tabindex="-1">
      
          Auto-injection
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/update-oneagent-on-aix/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/stop-restart-oneagent-on-aix/" tabindex="-1">
      
          Stop/restart OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/aix/operation/uninstall-oneagent-on-aix/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Related topics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-configuration-via-command-line-interface/" tabindex="-1">
      
          OneAgent configuration via command-line interface
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/android/" tabindex="-1">
      
          Android
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation via plugin
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/android-gradle-plugin/" tabindex="-1">
      
          Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/instrumentation-via-plugin/" tabindex="-1">
      
          Instrumentation via Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/monitoring-capabilities/" tabindex="-1">
      
          Monitoring capabilities of Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/configure-plugin-for-instrumentation/" tabindex="-1">
      
          Configure Dynatrace Android Gradle plugin for instrumentation processes
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/adjust-oneagent-configuration/" tabindex="-1">
      
          Use Dynatrace Android Gradle plugin to adjust OneAgent configuration
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/configure-multi-module-projects/" tabindex="-1">
      
          Configure multi-module Android projects with Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation via OneAgent sdk
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android/" tabindex="-1">
      
          OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/adjust-oneagent-communication/" tabindex="-1">
      
          Adjust communication with OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/manual-instrumentation/" tabindex="-1">
      
          Standalone manual instrumentation using OneAgent SDK for Android
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/troubleshooting/faqs/" tabindex="-1">
      
          Dynatrace Android Gradle plugin FAQs
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/troubleshooting/debug-logging-oneagent/" tabindex="-1">
      
          Debug logging for OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Legacy documentation
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Customization
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/oneagent-sdk-for-android/" tabindex="-1">
      
          OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/advanced-settings-for-android-auto-instrumentation/" tabindex="-1">
      
          Advanced settings
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/auto-instrumentation-properties-for-multidex-apps/" tabindex="-1">
      
          Auto-instrumentation properties for multidex apps
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/logging-for-android/" tabindex="-1">
      
          Logging
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/get-started-with-android-monitoring/" tabindex="-1">
      
          Get started with Android monitoring
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/dynatrace-auto-instrumentation-for-android/" tabindex="-1">
      
          Dynatrace auto-instrumentation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/dynatrace-gradle-plugin-for-android-app-auto-instrumentation/" tabindex="-1">
      
          Dynatrace Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/manual-instrumentation-for-android/" tabindex="-1">
      
          Manual instrumentation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/command-line-auto-instrumentation-for-android/" tabindex="-1">
      
          Command-line auto-instrumentation for Android
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/troubleshoot-oneagent-auto-instrumentation-on-android/" tabindex="-1">
      
          Instrumentation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/migration/" tabindex="-1">
      
          Migration
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/troubleshoot-monitoring-of-mobile-apps-on-android/" tabindex="-1">
      
          Monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/apache-cordova/" tabindex="-1">
      
          Apache Cordova
      
          </a>
        </span>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/" tabindex="-1">
      
          Cloud Foundry
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry/" tabindex="-1">
      
          Deploy OneAgent BOSH release
      
          </a>
        </span>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/monitoring/connect-your-cloud-foundry-foundations-to-dynatrace/" tabindex="-1">
      
          Monitor your clusters with Dynatrace
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/monitoring/cloud-foundry-metrics/" tabindex="-1">
      
          Cloud Foundry metrics overview
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Maintenance
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/update-oneagent-on-cloud-foundry/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/uninstall-oneagent-from-cloud-foundry/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/dynatrace-support-model-for-pivotal-platform/" tabindex="-1">
      
          Support lifecycle
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/maintenance/troubleshoot/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Other deployments and configurations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deployment-strategies/" tabindex="-1">
      
          Deployment strategies
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deploy-oneagent-on-ibm-cloud-foundry-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent on IBM Cloud Foundry
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deploy-oneagent-on-pivotal-web-services-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent on Pivotal Web Services
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent on SAP Cloud Platform
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/install-the-service-broker-for-cloud-foundry-dashboard-tile/" tabindex="-1">
      
          Install Dynatrace Service Broker
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/leverage-tags-defined-in-cloud-foundry-deployments/" tabindex="-1">
      
          Organize Cloud Foundry deployments by tags
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/define-process-group-metadata-for-cloud-foundry-applications/" tabindex="-1">
      
          Process group metadata for Cloud Foundry
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/" tabindex="-1">
      
          Google Cloud Platform
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/deploy-oneagent-for-google-app-engine-apps/" tabindex="-1">
      
          OneAgent on Google App Engine
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/google-kubernetes-engine/" tabindex="-1">
      
          OneAgent on Google Kubernetes Engine
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/google-cloud-platform/google-compute-engine/" tabindex="-1">
      
          OneAgent on Google Compute Engine
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/" tabindex="-1">
      
          Heroku
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation and operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/installation-and-operation/deploy-oneagent-on-heroku/" tabindex="-1">
      
          Deploy OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/installation-and-operation/update-oneagent-on-heroku/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/other-platforms/heroku/monitoring/monitor-your-heroku-applications/" tabindex="-1">
      
          Monitor your Heroku applications
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/ios/" tabindex="-1">
      
          iOS
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/instrumentation/get-started-with-ios-monitoring/" tabindex="-1">
      
          Get started with iOS monitoring
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/instrumentation/dynatrace-auto-instrumentation-for-ios/" tabindex="-1">
      
          Dynatrace auto-instrumentation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Customization
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/configuration-settings/" tabindex="-1">
      
          Configuration settings
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/oneagent-sdk-for-ios/" tabindex="-1">
      
          OneAgent SDK for iOS
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/logging-for-ios/" tabindex="-1">
      
          Logging
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/linux/" tabindex="-1">
      
          Linux
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux/" tabindex="-1">
      
          Disk space requirements
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/permission-requirements-for-oneagent-installation-and-operation-on-linux/" tabindex="-1">
      
          Permission requirements
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/install-oneagent-on-linux/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/install-oneagent-on-ppc-be-linux/" tabindex="-1">
      
          Install OneAgent on PPC BE Linux
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/customize-oneagent-installation-on-linux/" tabindex="-1">
      
          Customize installation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-linux/" tabindex="-1">
      
          How to pass a proxy address
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/oneagent-files-and-logs-on-linux/" tabindex="-1">
      
          OneAgent files and logs
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/update-oneagent-on-linux/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/update-oneagent-on-ppc-be-linux/" tabindex="-1">
      
          Update OneAgent on PPC BE Linux
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/stop-restart-oneagent-on-linux/" tabindex="-1">
      
          Stop/restart OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/operation/uninstall-oneagent-on-linux/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Related topics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/linux/related-topics/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor/" tabindex="-1">
      
          How to enable deep monitoring for applications confined by AppArmor
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-configuration-via-command-line-interface/" tabindex="-1">
      
          OneAgent configuration via command-line interface
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/" tabindex="-1">
      
          Microsoft Azure
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Azure Services
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/" tabindex="-1">
      
          Service monitoring
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-batch/" tabindex="-1">
      
          Azure Batch
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-db-mariadb/" tabindex="-1">
      
          Azure Database for MariaDB
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-db-mysql/" tabindex="-1">
      
          Azure Database for MySQL
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-db-postgresql/" tabindex="-1">
      
          Azure Database for PostgreSQL
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-front-door/" tabindex="-1">
      
          Azure Front Door
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-hdinsight/" tabindex="-1">
      
          Azure HDInsight
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-sql-managed-instance/" tabindex="-1">
      
          Azure SQL Managed Instance
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-traffic-manager/" tabindex="-1">
      
          Azure Traffic Manager
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-virtual-machines/" tabindex="-1">
      
          Azure Virtual Machines (classic)
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-monitoring/monitor-azure-virtual-network-gateways/" tabindex="-1">
      
          Azure Virtual Network Gateway
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machines/" tabindex="-1">
      
          Virtual Machines
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machines/deploy-oneagent-on-azure-virtual-machines/" tabindex="-1">
      
          Deploy OneAgent on Azure Virtual Machines
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machine-scale-sets/" tabindex="-1">
      
          Virtual Machine Scale Sets
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machine-scale-sets/deploy-oneagent-on-azure-vm-scaleset/" tabindex="-1">
      
          Deploy OneAgent on Azure Virtual Machine Scale Set
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/virtual-machine-scale-sets/troubleshoot-oneagent-deployment-on-azure-vm-scaleset/" tabindex="-1">
      
          Troubleshoot OneAgent deployment on Azure VM Scale Set
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-functions/" tabindex="-1">
      
          Azure Functions
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-functions/deploy-oneagent-on-azure-functions/" tabindex="-1">
      
          Deploy OneAgent on Azure Functions
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-monitor/" tabindex="-1">
      
          Azure Monitor
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-monitor/set-up-integration-for-azure-alerts/" tabindex="-1">
      
          Set up integration for Azure Alerts
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-monitor/set-up-integration-with-azure-monitor/" tabindex="-1">
      
          Set up integration with Azure Monitor
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/" tabindex="-1">
      
          App Service
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/deploy-oneagent-on-azure-app-service/" tabindex="-1">
      
          Deploy OneAgent on Azure App Service
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/update-oneagent-on-azure-app-service/" tabindex="-1">
      
          Update OneAgent on Azure App Service
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/troubleshoot-oneagent-deployment-on-azure-app-service/" tabindex="-1">
      
          Troubleshoot OneAgent deployment on Azure App Service
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/app-service/uninstall-oneagent-from-azure-app-service/" tabindex="-1">
      
          Uninstall OneAgent from Azure App Service
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/service-fabric/" tabindex="-1">
      
          Service Fabric
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/microsoft-azure/azure-services/azure-kubernetes-service/" tabindex="-1">
      
          Azure Kubernetes Service
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/windows/" tabindex="-1">
      
          Windows
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows/" tabindex="-1">
      
          Disk space requirements
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/permission-requirements-for-oneagent-installation-and-operation-on-windows/" tabindex="-1">
      
          Permission requirements
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/install-oneagent-on-windows/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/customize-oneagent-installation-on-windows/" tabindex="-1">
      
          Customize installation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows/" tabindex="-1">
      
          How to pass a proxy address
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/oneagent-files-and-logs-on-windows/" tabindex="-1">
      
          OneAgent files and logs
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/update-oneagent-on-windows/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/stop-restart-oneagent-on-windows/" tabindex="-1">
      
          Stop/restart OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/windows/operation/uninstall-oneagent-on-windows/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Related topics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-oneagent/oneagent-configuration-via-command-line-interface/" tabindex="-1">
      
          OneAgent configuration via command-line interface
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/cloud-platforms/openshift/" tabindex="-1">
      
          Red Hat OpenShift
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/deploy-oneagent-openshift/" tabindex="-1">
      
          Deploy OneAgent Operator
      
          </a>
        </span>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/monitor-openshift-clusters-with-dynatrace/" tabindex="-1">
      
          Monitor your clusters with Dynatrace
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/monitor-openshift-cluster-utilization/" tabindex="-1">
      
          Cluster utilization
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/events/" tabindex="-1">
      
          Events
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/monitoring/monitor-workloads-openshift/" tabindex="-1">
      
          Workloads
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Maintenance
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/update-oneagent-on-openshift/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/uninstall-oneagent-from-openshift/" tabindex="-1">
      
          Uninstall OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/migrate-tenant-openshift/" tabindex="-1">
      
          Migrate OneAgent Operator to a new Dynatrace OpenShift tenant
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/dynatrace-support-model-for-openshift/" tabindex="-1">
      
          Support lifecycle
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/maintenance/troubleshoot-oneagent-on-openshift/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Other deployments and configurations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/openshift-deployment-strategies/" tabindex="-1">
      
          Deployment strategies
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/deploy-daemonset/" tabindex="-1">
      
          Deploy OneAgent Daemonset
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/deploy-oneagent-on-openshift-for-application-only-monitoring/" tabindex="-1">
      
          Deploy OneAgent for application-only monitoring
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/deploy-with-operatorhub/" tabindex="-1">
      
          Deploy OneAgent via OperatorHub
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/oneagent-in-airgapped-openshift-environment/" tabindex="-1">
      
          Prerequisites for air-gapped clusters
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/leverage-tags-defined-in-openshift-deployments/" tabindex="-1">
      
          Organize OpenShift deployments by tags
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/configure-istio-for-oneagent-traffic-in-openshift/" tabindex="-1">
      
          Configure Istio
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/solaris/" tabindex="-1">
      
          Solaris
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/solaris/installation/install-oneagent-on-solaris/" tabindex="-1">
      
          Install OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/solaris/operation/update-oneagent-on-solaris/" tabindex="-1">
      
          Update OneAgent
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/solaris/operation/troubleshoot-oneagent-installation-on-solaris/" tabindex="-1">
      
          Troubleshoot
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/xamarin/" tabindex="-1">
      
          Xamarin
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/" tabindex="-1">
      
          Dynatrace ActiveGate
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/basic-concepts/when-do-i-need-to-install-an-activegate/" tabindex="-1">
      
          When do I need to install an ActiveGate?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/basic-concepts/supported-connectivity-schemes-for-activegates/" tabindex="-1">
      
          Supported connectivity schemes for ActiveGates
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/installation/activegate-hardware-and-system-requirements/" tabindex="-1">
      
          ActiveGate hardware and system requirements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/installation/install-an-environment-activegate/" tabindex="-1">
      
          Install an Environment ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/installation/customize-installation-for-activegate/" tabindex="-1">
      
          Customize ActiveGate installation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/operation/stop-restart-activegate/" tabindex="-1">
      
          Stop/restart ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/operation/update-activegate/" tabindex="-1">
      
          Update ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/operation/uninstall-activegate/" tabindex="-1">
      
          Uninstall ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/operation/troubleshoot-activegate/" tabindex="-1">
      
          Troubleshoot ActiveGate
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/" tabindex="-1">
      
          Configuration
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/configure-activegate/" tabindex="-1">
      
          Configure ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate/" tabindex="-1">
      
          Configure trusted root certificates on ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/where-can-i-find-activegate-files/" tabindex="-1">
      
          Where can I find ActiveGate files?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/which-network-ports-does-activegate-use/" tabindex="-1">
      
          Which network ports does ActiveGate use?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/configure-activegate-launcher/" tabindex="-1">
      
          Configure ActiveGate launcher
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate/" tabindex="-1">
      
          Setting up a proxy for ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate/" tabindex="-1">
      
          Setting up reverse proxy for ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support/" tabindex="-1">
      
          Configure an Environment ActiveGate for multi-environment support
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/how-to-configure-ciphers-on-activegate/" tabindex="-1">
      
          How to configure ciphers on ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate/" tabindex="-1">
      
          Configure custom SSL certificate on ActiveGate
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/network-zones/" tabindex="-1">
      
          Network zones
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/network-zones-basic-info/" tabindex="-1">
      
          Basic info
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/oneagent-connectivity/" tabindex="-1">
      
          OneAgent connectivity
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/activegate-connectivity/" tabindex="-1">
      
          ActiveGate connectivity
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/network-zones/migration/" tabindex="-1">
      
          Migration
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/migration/analyze/" tabindex="-1">
      
          Analyze
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/migration/plan/" tabindex="-1">
      
          Plan
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/migration/deploy/" tabindex="-1">
      
          Deploy
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/migration/verify/" tabindex="-1">
      
          Verify
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/network-zones/new-installation/" tabindex="-1">
      
          New installation
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/new-installation/analyze/" tabindex="-1">
      
          Analyze
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/new-installation/plan/" tabindex="-1">
      
          Plan
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/new-installation/deploy/" tabindex="-1">
      
          Deploy
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/new-installation/verify/" tabindex="-1">
      
          Verify
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/rename-network-zone/" tabindex="-1">
      
          Rename a network zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/network-zones/delete-network-zones/" tabindex="-1">
      
          Delete a network zone
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/integrations/" tabindex="-1">
      
          Integrations
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/integrations/dynatrace-modules/" tabindex="-1">
      
          Dynatrace modules
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Appmon
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/link-purepaths-between-dynatrace-appmon/" tabindex="-1">
      
          Link PurePaths between Dynatrace and AppMon
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/incorporate-appmon-data-into-dynatrace/" tabindex="-1">
      
          Incorporate AppMon monitoring data into Dynatrace
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Nam
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/dynatrace-modules/nam/integrate-num-and-network-monitoring/" tabindex="-1">
      
          Integrate NAM and network monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/" tabindex="-1">
      
          3rd Party integrations
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Problem notification systems
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/email-integration/" tabindex="-1">
      
          Email
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/webhook-integration/" tabindex="-1">
      
          Webhook
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/servicenow-integration/" tabindex="-1">
      
          ServiceNow
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/jira-integration/" tabindex="-1">
      
          JIRA
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/opsgenie-integration/" tabindex="-1">
      
          OpsGenie
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/pagerduty-integration/" tabindex="-1">
      
          PagerDuty
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/victorops-integration/" tabindex="-1">
      
          VictorOps
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/microsoft-teams-integration/" tabindex="-1">
      
          Microsoft Teams
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/slack-integration/" tabindex="-1">
      
          Slack
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/xmatters-integration/" tabindex="-1">
      
          xMatters
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Test automation frameworks
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/dynatrace-and-load-testing-tools-integration/" tabindex="-1">
      
          Load testing tools
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/dynatrace-and-loadrunner-integration/" tabindex="-1">
      
          LoadRunner
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/dynatrace-and-jmeter-integration/" tabindex="-1">
      
          JMeter
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/neotys-integration/" tabindex="-1">
      
          Neotys
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Deployment automation frameworks
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/integrations/third-party-integrations/deployment-automation-frameworks/dynatrace-and-ansible-tower-integration/" tabindex="-1">
      
          Ansible Tower
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Extend Dynatrace
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/extend-dynatrace/extensions/" tabindex="-1">
      
          Extensions
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          ActiveGate extensions
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/activegate-extensions/introduction-to-activegate-plugins/" tabindex="-1">
      
          Introduction to ActiveGate extensions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/activegate-extensions/activegate-plugins-capabilities/" tabindex="-1">
      
          ActiveGate extension capabilities
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/activegate-extensions/write-your-first-activegate-plugin/" tabindex="-1">
      
          ActiveGate extensions tutorial
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Development
      
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-sdk-commands/" tabindex="-1">
      
          Extension SDK commands
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/install-extension-sdk/" tabindex="-1">
      
          Install extension SDK
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/install-activegate-plugin-module/" tabindex="-1">
      
          Install ActiveGate plugin module
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/" tabindex="-1">
      
          Extensions How-tos
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/deploy-an-activegate-plugin/" tabindex="-1">
      
          Deploy an extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/charts/" tabindex="-1">
      
          Charts
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/key-performance-metrics/" tabindex="-1">
      
          Key performance metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/alerting/" tabindex="-1">
      
          Extensions alerting
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/group-metrics/" tabindex="-1">
      
          Group metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/state-metrics/" tabindex="-1">
      
          State metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/activegate-plugin-module-custom-configuration/" tabindex="-1">
      
          ActiveGate plugin module custom configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/extension-configuration/" tabindex="-1">
      
          Extension configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/topology/" tabindex="-1">
      
          Topology
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/problems-and-events/" tabindex="-1">
      
          Problems and events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/extension-how-tos/custom-properties/" tabindex="-1">
      
          Custom properties
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/development/use-external-python-packages/" tabindex="-1">
      
          How to use external Python packages
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          JMX extensions
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/jmx-extensions/customize-jmx-extensions/" tabindex="-1">
      
          Customize JMX extensions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/jmx-extensions/jmx-extensions/" tabindex="-1">
      
          JMX extensions
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          OneAgent extensions
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/oneagent-extensions/oneagent-extensions-hands-on/" tabindex="-1">
      
          OneAgent extensions tutorial
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Reference
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Json reference
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/reference/json-reference/extension-json-explained/" tabindex="-1">
      
          Extension JSON explained
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/reference/json-reference/extension-json-reference/" tabindex="-1">
      
          Extension JSON reference
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/reference/python-reference/" tabindex="-1">
      
          Extension Python API reference
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/troubleshooting/extension-sdk-performance/" tabindex="-1">
      
          ActiveGate plugin module performance
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/troubleshooting/troubleshoot-extensions/" tabindex="-1">
      
          Troubleshoot extensions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/troubleshooting/extension-simulator/" tabindex="-1">
      
          Extension simulator
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/troubleshooting/frequently-asked-questions/" tabindex="-1">
      
          ActiveGate extension FAQs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/extensions/troubleshooting/activegate-plugins-limitations/" tabindex="-1">
      
          Extensions limitations
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/extend-dynatrace/openkit/" tabindex="-1">
      
          Dynatrace OpenKit
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Installation and operation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/openkit/installation-and-operation/instrument-your-application-using-dynatrace-openkit/" tabindex="-1">
      
          Instrument your application using Dynatrace OpenKit
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/openkit/installation-and-operation/dynatrace-openkit-libraries-on-github/" tabindex="-1">
      
          Dynatrace OpenKit libraries on GitHub
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/openkit/installation-and-operation/dynatrace-openkit-api-methods/" tabindex="-1">
      
          Dynatrace OpenKit API methods
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/openkit/installation-and-operation/dynatrace-openkit-logging/" tabindex="-1">
      
          Dynatrace OpenKit logging
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/openkit/installation-and-operation/troubleshoot-dynatrace-openkit-instrumentation/" tabindex="-1">
      
          Troubleshoot Dynatrace OpenKit instrumentation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Related topics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="https://www.dynatrace.com/news/blog/monitoring-the-microsoft-hololens-experience-with-dynatrace-openkit/" tabindex="-1">
      
          Monitoring the Microsoft HoloLens experience with Dynatrace OpenKit
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/oneagent-sdk/" tabindex="-1">
      
          OneAgent SDK
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/extend-dynatrace/custom-metric-ingestion-and-analysis/" tabindex="-1">
      
          Custom metric ingestion and analysis
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          How to use Dynatrace
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/" tabindex="-1">
      
          Real User Monitoring
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic RUM concepts
      
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/applications/" tabindex="-1">
      
          Applications
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/user-actions/" tabindex="-1">
      
          User actions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/user-session/" tabindex="-1">
      
          User sessions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/user-action-metrics/" tabindex="-1">
      
          User action metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/rum-javascript-injection/" tabindex="-1">
      
          RUM JavaScript injection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/detection-of-ip-addresses-locations-and-user-agents/" tabindex="-1">
      
          Detection of IP addresses, geolocations, and user agents
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/ratings/" tabindex="-1">
      
          Dynatrace scores and ratings
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/ratings/apdex-ratings/" tabindex="-1">
      
          Apdex ratings
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/ratings/user-experience-score/" tabindex="-1">
      
          User experience score
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/basic-concepts/session-replay/" tabindex="-1">
      
          Session Replay
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Setup and configuration of RUM
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Web applications
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Initial configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/initial-configuration/define-your-applications-via-the-my-web-application-placeholder/" tabindex="-1">
      
          Define your applications via the `My web application` placeholder
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/initial-configuration/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions/" tabindex="-1">
      
          Configure Real User Monitoring to capture XHR actions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/initial-configuration/set-up-amp-monitoring/" tabindex="-1">
      
          Set up AMP monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/initial-configuration/create-custom-names-for-user-actions/" tabindex="-1">
      
          Create custom names for user actions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/initial-configuration/firewall-constraints-for-rum/" tabindex="-1">
      
          Firewall constraints for RUM
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Additional configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr/" tabindex="-1">
      
          Configure Real User Monitoring according to GDPR
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/configure-session-replay-for-personal-data-protection/" tabindex="-1">
      
          Configure Session Replay
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/map-internal-ip-addresses-to-locations/" tabindex="-1">
      
          Map internal IP addresses to locations
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection/" tabindex="-1">
      
          Configure 3rd-party and CDN content detection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/customize-ip-address-detection/" tabindex="-1">
      
          Customize IP address detection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/enable-session-replay/" tabindex="-1">
      
          Enable Session Replay
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/configure-beacon-domain-whitelist/" tabindex="-1">
      
          Configure beacon domain allow list
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/define-user-action-and-session-properties/" tabindex="-1">
      
          Define user action and session properties
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring/" tabindex="-1">
      
          Exclude browsers, robots, and spiders from monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/configure-your-caching-servers/" tabindex="-1">
      
          Configure your caching servers
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie/" tabindex="-1">
      
          Configure XHR for older versions of IE
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/export-session-data/" tabindex="-1">
      
          Export user session data
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/customize-rum/" tabindex="-1">
      
          Customize Real User Monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/configure-errors/" tabindex="-1">
      
          Configure your application to ignore errors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/application-detection-rules/" tabindex="-1">
      
          Application detection rules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/rum-calculated-metrics/" tabindex="-1">
      
          Calculated metrics for Real User Monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/additional-configuration/modify-csp-for-rum/" tabindex="-1">
      
          Modify Content Security Policy for RUM
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Alternative setup
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/alternative-setup/set-up-the-rum-browser-extension/" tabindex="-1">
      
          Set up the RUM browser extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/alternative-setup/set-up-agentless-real-user-monitoring/" tabindex="-1">
      
          Set up agentless Real User Monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/troubleshooting/why-dont-i-see-my-applications-or-monitoring-data/" tabindex="-1">
      
          Why don&apos;t I see my applications or monitoring data?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/troubleshooting/what-does-a-max-user-actions-per-minute-exceeded-message-mean/" tabindex="-1">
      
          What does a &apos;Max. user actions per minute exceeded&apos; message mean?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/troubleshooting/capture-https-sessions-for-debugging-using-fiddler/" tabindex="-1">
      
          Capture HTTP/HTTPS sessions for debugging using Fiddler
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/troubleshooting/beacon-forwarder/" tabindex="-1">
      
          Use Dynatrace infrastructure as endpoint for RUM monitoring signals
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Mobile apps
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Additional configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/mobile-apps/additional-configuration/configure-cost-and-traffic-control/" tabindex="-1">
      
          Configure cost and traffic control for mobile app monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/mobile-apps/additional-configuration/oneagent-as-beacon-forwarder/" tabindex="-1">
      
          Use OneAgent as a beacon endpoint
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation of mobile RUM
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/android/" tabindex="-1">
      
          Instrument your Android app
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation via plugin
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/android-gradle-plugin/" tabindex="-1">
      
          Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/instrumentation-via-plugin/" tabindex="-1">
      
          Instrumentation via Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/monitoring-capabilities/" tabindex="-1">
      
          Monitoring capabilities of Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/configure-plugin-for-instrumentation/" tabindex="-1">
      
          Configure Dynatrace Android Gradle plugin for instrumentation processes
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/adjust-oneagent-configuration/" tabindex="-1">
      
          Use Dynatrace Android Gradle plugin to adjust OneAgent configuration
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-plugin/configure-multi-module-projects/" tabindex="-1">
      
          Configure multi-module Android projects with Dynatrace Android Gradle plugin
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation via OneAgent sdk
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android/" tabindex="-1">
      
          OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/adjust-oneagent-communication/" tabindex="-1">
      
          Adjust communication with OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/instrumentation-via-oneagent-sdk/manual-instrumentation/" tabindex="-1">
      
          Standalone manual instrumentation using OneAgent SDK for Android
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/troubleshooting/faqs/" tabindex="-1">
      
          Dynatrace Android Gradle plugin FAQs
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/troubleshooting/debug-logging-oneagent/" tabindex="-1">
      
          Debug logging for OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Legacy documentation
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Customization
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/oneagent-sdk-for-android/" tabindex="-1">
      
          OneAgent SDK for Android
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/advanced-settings-for-android-auto-instrumentation/" tabindex="-1">
      
          Advanced settings
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/auto-instrumentation-properties-for-multidex-apps/" tabindex="-1">
      
          Auto-instrumentation properties for multidex apps
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/customization/logging-for-android/" tabindex="-1">
      
          Logging
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/get-started-with-android-monitoring/" tabindex="-1">
      
          Get started with Android monitoring
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/dynatrace-auto-instrumentation-for-android/" tabindex="-1">
      
          Dynatrace auto-instrumentation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/dynatrace-gradle-plugin-for-android-app-auto-instrumentation/" tabindex="-1">
      
          Dynatrace Gradle plugin
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/manual-instrumentation-for-android/" tabindex="-1">
      
          Manual instrumentation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/instrumentation/command-line-auto-instrumentation-for-android/" tabindex="-1">
      
          Command-line auto-instrumentation for Android
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/troubleshoot-oneagent-auto-instrumentation-on-android/" tabindex="-1">
      
          Instrumentation
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/migration/" tabindex="-1">
      
          Migration
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/android/legacy-documentation/troubleshooting/troubleshoot-monitoring-of-mobile-apps-on-android/" tabindex="-1">
      
          Monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/technology-support/operating-systems/ios/" tabindex="-1">
      
          Instrument your iOS app
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Instrumentation
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/instrumentation/get-started-with-ios-monitoring/" tabindex="-1">
      
          Get started with iOS monitoring
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/instrumentation/dynatrace-auto-instrumentation-for-ios/" tabindex="-1">
      
          Dynatrace auto-instrumentation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children is-reference" role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Customization
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/configuration-settings/" tabindex="-1">
      
          Configuration settings
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/oneagent-sdk-for-ios/" tabindex="-1">
      
          OneAgent SDK for iOS
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/operating-systems/ios/customization/logging-for-ios/" tabindex="-1">
      
          Logging
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting mobile RUM
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/troubleshooting/what-does-a-max-user-actions-per-minute-exceeded-message-mean/" tabindex="-1">
      
          What does a &apos;Max. user actions per minute exceeded&apos; message mean?
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Applications empowered by OpenKit (custom applications)
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Troubleshooting RUM for custom applications
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/setup-and-configuration/web-applications/troubleshooting/what-does-a-max-user-actions-per-minute-exceeded-message-mean/" tabindex="-1">
      
          What does a &apos;Max. user actions per minute exceeded&apos; message mean?
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          How to use Real User Monitoring
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Web applications
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/introduction-to-application-overview/" tabindex="-1">
      
          Introduction to application overview page
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/performance-analysis/" tabindex="-1">
      
          Performance analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/user-behavior-analysis/" tabindex="-1">
      
          User behavior analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/multi-dimensional-analysis/" tabindex="-1">
      
          Multidimensional analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/waterfall-analysis/" tabindex="-1">
      
          Waterfall analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/world-map-view/" tabindex="-1">
      
          World map view
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/source-map-support-for-javascript-error-analysis/" tabindex="-1">
      
          Source map support for JavaScript error analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/analyze-individual-user-actions/" tabindex="-1">
      
          Analyze individual user actions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/work-with-key-performance-metrics/" tabindex="-1">
      
          Work with key performance metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/define-conversion-goals/" tabindex="-1">
      
          Define conversion goals
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/how-to-use-visually-complete-and-speed-index-metrics/" tabindex="-1">
      
          How to use &quot;Visually complete&quot; and &quot;Speed index&quot; metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/visually-complete-top-findings/" tabindex="-1">
      
          Visually complete top findings
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/leverage-user-session-properties/" tabindex="-1">
      
          Leverage user session properties
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/application-analysis-with-hyperlyzer/" tabindex="-1">
      
          Application analysis with Hyperlyzer
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/web-applications/service-flows-for-applications-and-user-actions/" tabindex="-1">
      
          Service flows for applications and user actions
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Mobile and custom applications
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/mobile-and-custom-applications/mobile-user-session-analysis/" tabindex="-1">
      
          Mobile user session analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/mobile-and-custom-applications/check-usage-metrics-for-a-mobile-app/" tabindex="-1">
      
          Check usage metrics for a mobile app
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/mobile-and-custom-applications/analyze-http-performance-and-error-rates-for-mobile-apps/" tabindex="-1">
      
          Analyze network performance and error rates for mobile apps
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/mobile-and-custom-applications/mobile-crash-reports/" tabindex="-1">
      
          Crash reports for mobile apps
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/mobile-and-custom-applications/upload-and-manage-symbol-files/" tabindex="-1">
      
          Upload and manage symbol files
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/mobile-and-custom-applications/js-tag-api/" tabindex="-1">
      
          Download and use the JavaScript tag API
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Cross application user session analytics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/cross-application-user-session-analytics/user-session-analysis/" tabindex="-1">
      
          User session analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/cross-application-user-session-analytics/custom-queries-segmentation-and-aggregation-of-session-data/" tabindex="-1">
      
          Custom queries, segmentation, and aggregation of session data
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/cross-application-user-session-analytics/analyze-all-sessions-of-a-single-user/" tabindex="-1">
      
          Analyze all sessions of a single user
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/real-user-monitoring/how-to-use-real-user-monitoring/cross-application-user-session-analytics/identify-individual-users-for-session-analysis/" tabindex="-1">
      
          Identify individual users for session analysis
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/" tabindex="-1">
      
          Synthetic Monitoring
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          General information
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/general-information/types-of-synthetic-monitors/" tabindex="-1">
      
          Types of synthetic monitors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/general-information/synthetic-calculations/" tabindex="-1">
      
          Synthetic calculations
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/general-information/credential-vault-for-synthetic-monitors/" tabindex="-1">
      
          Credential vault for synthetic monitors
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Browser monitors
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor/" tabindex="-1">
      
          Create a single-URL browser monitor
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/browser-monitors/record-a-browser-clickpath/" tabindex="-1">
      
          Record a browser clickpath
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/browser-monitors/configure-browser-monitors/" tabindex="-1">
      
          Configure browser monitors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/browser-monitors/browser-clickpath-events/" tabindex="-1">
      
          Browser clickpath events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration/" tabindex="-1">
      
          Script mode for browser monitor configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/browser-monitors/browser-monitor-issues-with-content-security-policy/" tabindex="-1">
      
          Browser monitor issues with Content Security Policy
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths/" tabindex="-1">
      
          Number of actions consumed by browser clickpaths
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          HTTP monitors
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/http-monitors/create-an-http-monitor/" tabindex="-1">
      
          Create an HTTP monitor
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/http-monitors/configure-http-monitors/" tabindex="-1">
      
          Configure HTTP monitors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/http-monitors/pre-and-post-scripting-for-http-monitors/" tabindex="-1">
      
          Pre and post scripting
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/http-monitors/script-mode-for-http-monitor-configuration/" tabindex="-1">
      
          Script mode
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Private synthetic locations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic/" tabindex="-1">
      
          Requirements for private synthetic locations
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location/" tabindex="-1">
      
          Create a private synthetic location
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic/" tabindex="-1">
      
          Set up a proxy for private synthetic monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Analysis and alerting
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/analysis-and-alerting/synthetic-alerting-overview/" tabindex="-1">
      
          Synthetic alerting overview
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors/" tabindex="-1">
      
          Synthetic details for browser monitors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors/" tabindex="-1">
      
          Multidimensional analysis for browser monitors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/synthetic-monitoring/analysis-and-alerting/waterfall-graphs/" tabindex="-1">
      
          Waterfall graphs
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/" tabindex="-1">
      
          Data privacy and security
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Data privacy
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-privacy/data-protection/" tabindex="-1">
      
          Data protection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-privacy/data-retention-periods/" tabindex="-1">
      
          Data retention periods
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace/" tabindex="-1">
      
          Personal data captured by Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-privacy/levels-of-data-protection/" tabindex="-1">
      
          Levels of data protection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-privacy/cookies/" tabindex="-1">
      
          Cookies
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-privacy/dynatrace-compliance-with-gdpr-for-eu-citizens/" tabindex="-1">
      
          Dynatrace compliance with GDPR for EU citizens
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-privacy/custom-privacy-policy-for-dynatrace-real-user-monitoring/" tabindex="-1">
      
          Custom privacy policy for Dynatrace Real User Monitoring
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/data-privacy/data-exchange-between-a-managed-cluster-and-mission-control/" tabindex="-1">
      
          Data privacy and exchange in Managed deployments
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/setup-and-configuration/dynatrace-managed/data-privacy/monitored-technologies/" tabindex="-1">
      
          Monitored technologies and feature usage
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Data security
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-security/report-a-security-related-concern/" tabindex="-1">
      
          Report a security-related concern
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-security/data-security-controls/" tabindex="-1">
      
          Data security controls
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/data-security/secure-development-controls/" tabindex="-1">
      
          Secure development controls
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/configuration/configure-dynatrace-to-protect-personal-data/" tabindex="-1">
      
          Configure Dynatrace to protect personal data
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/configuration/configure-global-privacy-settings/" tabindex="-1">
      
          Configure global privacy settings
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/data-privacy-and-security/configuration/audit-logs/" tabindex="-1">
      
          Audit logs
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/" tabindex="-1">
      
          Transactions and services
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/basic-concepts/scope-and-usage-of-services/" tabindex="-1">
      
          Scope and usage of services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/basic-concepts/service-detection-and-naming/" tabindex="-1">
      
          Service detection and naming
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/basic-concepts/merged-services/" tabindex="-1">
      
          Merged services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/basic-concepts/opaque-services/" tabindex="-1">
      
          Opaque services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/basic-concepts/request-attributes/" tabindex="-1">
      
          Request attributes
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Analysis
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/service-analysis-types/" tabindex="-1">
      
          Service analysis types
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/cpu-analysis/" tabindex="-1">
      
          CPU analysis
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/top-web-requests/" tabindex="-1">
      
          Top web requests
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/response-time-distribution-and-outlier-analysis/" tabindex="-1">
      
          Response time distribution and outlier analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/service-response-time-hotspots/" tabindex="-1">
      
          Service response time hotspots
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/service-flow/" tabindex="-1">
      
          Service flow
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/service-flow-filtering/" tabindex="-1">
      
          Service flow filtering
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/filter-monitoring-data-via-request-attributes/" tabindex="-1">
      
          Filter monitoring data via request attributes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/service-backtrace/" tabindex="-1">
      
          Service backtrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/purepath-visualization/" tabindex="-1">
      
          PurePath visualization
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/purepath-capture-errors/" tabindex="-1">
      
          PurePath capture errors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/context-specific-drill-down/" tabindex="-1">
      
          Context-specific drill down
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/analyze-individual-service-instances/" tabindex="-1">
      
          Analyze individual service instances
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/analysis/memory-profiling/" tabindex="-1">
      
          Memory profiling
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/service-monitoring-settings/" tabindex="-1">
      
          Service monitoring settings
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/customize-service-naming/" tabindex="-1">
      
          Customize service naming
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/set-up-web-request-naming-using-request-attributes/" tabindex="-1">
      
          Set up request naming using request attributes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/configure-service-error-detection/" tabindex="-1">
      
          Configure service error detection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/capture-request-attributes-based-on-web-request-data/" tabindex="-1">
      
          Capture request attributes based on web request data
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/capture-request-attributes-based-on-method-arguments/" tabindex="-1">
      
          Capture request attributes based on method arguments
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/define-custom-services/" tabindex="-1">
      
          Define custom services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/define-messaging-services/" tabindex="-1">
      
          Define queue messaging consuming custom services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/configuration/customize-api-definitions/" tabindex="-1">
      
          Custom API definitions
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/monitoring/how-to-start-service-monitoring/" tabindex="-1">
      
          How to start service monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/monitoring/where-can-i-monitor-my-services/" tabindex="-1">
      
          Service health tile
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/monitoring/monitor-key-requests/" tabindex="-1">
      
          Monitor key requests
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/monitoring/create-custom-charts-based-on-request-attributes/" tabindex="-1">
      
          Create custom charts based on request attributes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/monitoring/monitor-3rd-party-services/" tabindex="-1">
      
          Monitor 3rd party services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/transactions-and-services/monitoring/adaptive-traffic-management-and-control/" tabindex="-1">
      
          Adaptive traffic management and control
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/databases/" tabindex="-1">
      
          Databases
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Introduction
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/databases/introduction/how-database-activity-is-monitored/" tabindex="-1">
      
          How database activity is monitored
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/databases/introduction/support-for-sql-bind-variables/" tabindex="-1">
      
          Support for SQL bind variables
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Analysis
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/databases/analysis/analyze-database-services/" tabindex="-1">
      
          Analyze database services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/databases/analysis/improve-database-performance/" tabindex="-1">
      
          Improve database performance
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/databases/analysis/database-insights/" tabindex="-1">
      
          Oracle database insights
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/process-groups/" tabindex="-1">
      
          Process groups
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/basic-concepts/which-are-the-most-important-processes/" tabindex="-1">
      
          Which are the most important processes?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/basic-concepts/what-technologies-underlie-individual-processes/" tabindex="-1">
      
          What technologies underlie individual processes?
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/configuration/set-up-process-group-monitoring/" tabindex="-1">
      
          Set up process group monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/configuration/adapt-the-composition-of-default-process-groups/" tabindex="-1">
      
          Customize the structure of process groups
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/configuration/customize-the-name-of-process-groups/" tabindex="-1">
      
          Customize the names of process groups
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/configuration/define-your-own-process-group-metadata/" tabindex="-1">
      
          Define your own process group metadata
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment/" tabindex="-1">
      
          Overview of all technologies running in your environment
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/monitoring/analyze-processes/" tabindex="-1">
      
          Analyze processes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/monitoring/analyze-process-responsiveness/" tabindex="-1">
      
          Analyze process responsiveness
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/monitoring/process-group-availability-monitoring-and-alerting/" tabindex="-1">
      
          Process group availability monitoring and alerting
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/monitoring/monitor-process-specific-network-connections/" tabindex="-1">
      
          Monitor process-specific network connections
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/hosts/" tabindex="-1">
      
          Hosts
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/basic-concepts/get-started-with-infrastructure-monitoring/" tabindex="-1">
      
          Get started with infrastructure monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/basic-concepts/how-effective-is-infrastructure-monitoring-on-its-own/" tabindex="-1">
      
          How effective is infrastructure monitoring on its own?
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/configuration/organize-your-environment-using-host-groups/" tabindex="-1">
      
          Organize your environment using host groups
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/configuration/set-custom-host-names-in-dynamic-environments/" tabindex="-1">
      
          Set custom host names in dynamic environments
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/configuration/define-tags-and-metadata-for-hosts/" tabindex="-1">
      
          Define tags and metadata for hosts
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Monitoring
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/monitoring/measures-for-host-health/" tabindex="-1">
      
          Measures for host health
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/monitoring/where-can-i-view-host-performance-measures/" tabindex="-1">
      
          Where can I view host performance measures?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/monitoring/windows-services/" tabindex="-1">
      
          Windows services availability
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/" tabindex="-1">
      
          Log Monitoring
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/basic-concepts/log-monitoring-functionality/" tabindex="-1">
      
          Log Monitoring functionality
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/basic-concepts/auto-discovery-of-log-content/" tabindex="-1">
      
          Log content auto-discovery
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/basic-concepts/what-log-format-does-log-analytics-support/" tabindex="-1">
      
          Log file formats
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/basic-concepts/log-analytics-data-storage/" tabindex="-1">
      
          Log data storage
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Log analysis
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/log-analysis/analyze-log-data-and-create-events/" tabindex="-1">
      
          Analyze log data
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/log-analysis/search-patterns-in-log-data-ad-parese-results/" tabindex="-1">
      
          Search patterns in log data and parse results
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/log-analysis/custom-metrics-for-log-monitoring/" tabindex="-1">
      
          Custom metrics for log monitoring
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/configuration/how-to-enable-log-analytics/" tabindex="-1">
      
          Enable Log Monitoring
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/configuration/enable-access-to-log-content/" tabindex="-1">
      
          Enable access to log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/configuration/add-log-files-manually/" tabindex="-1">
      
          Add log files manually
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/configuration/log-analytics-configuration-file/" tabindex="-1">
      
          Log Monitoring configuration file
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/log-monitoring/configuration/mask-sensitive-information-in-log-analytics/" tabindex="-1">
      
          Mask sensitive information in logs
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/networks/" tabindex="-1">
      
          Networks
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/networks/how-to-monitor-network-communication/" tabindex="-1">
      
          How to monitor network communications
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/networks/detect-network-errors/" tabindex="-1">
      
          Detect network errors
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/" tabindex="-1">
      
          Dashboards and charts
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Dashboards
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/dashboards/create-dashboards/" tabindex="-1">
      
          Create dashboards
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/dashboards/organize-dashboards/" tabindex="-1">
      
          Organize dashboards
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/dashboards/share-dashboards/" tabindex="-1">
      
          Share dashboards
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/dashboards/dashboard-timeframe/" tabindex="-1">
      
          Timeframe and management zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/dashboards/subscribe-to-dashboard-reports/" tabindex="-1">
      
          Dashboard reports
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Custom charts and tiles
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/custom-charts-and-tiles/custom-charts/" tabindex="-1">
      
          Custom charts
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/custom-charts-and-tiles/custom-charts/chart-types/" tabindex="-1">
      
          Chart types
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/custom-charts-and-tiles/pin-tiles-to-your-dashboard/" tabindex="-1">
      
          Pin tiles to your dashboard
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/custom-charts-and-tiles/filter-charts/" tabindex="-1">
      
          Filter charts
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/dashboards-and-charts/custom-charts-and-tiles/markdown-tile/" tabindex="-1">
      
          Markdown tile
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/reports/" tabindex="-1">
      
          Reports
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/reports/service-quality-reports/" tabindex="-1">
      
          Service quality reports
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/" tabindex="-1">
      
          Davis Assistant
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/basic-concepts/get-started-with-davis-assistant/" tabindex="-1">
      
          Get started with Davis Assistant
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/basic-concepts/interact-with-davis-assistant-on-the-web/" tabindex="-1">
      
          Davis Assistant Web
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/basic-concepts/davis-assistant-data-security/" tabindex="-1">
      
          Davis Assistant data security
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Configuration
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/configuration/add-a-dynatrace-environment-to-davis-assistant/" tabindex="-1">
      
          Add a Dynatrace environment to Davis Assistant
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/configuration/enable-davis-assistant-charts/" tabindex="-1">
      
          Enable Davis Assistant charts
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/configuration/manage-users-programmatically/" tabindex="-1">
      
          Manage users programmatically
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/configuration/filter-davis-assistant-interactions-using-tags/" tabindex="-1">
      
          Tag-based filtering
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Integrations
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/integrations/davis-assistant-for-alexa/" tabindex="-1">
      
          Amazon Alexa
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/integrations/davis-assistant-for-google-assistant/" tabindex="-1">
      
          Google Assistant
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/integrations/dynatrace-voice-navigation-with-davis-assistant/" tabindex="-1">
      
          Voice Navigator
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/integrations/davis-assistant-for-slack/" tabindex="-1">
      
          Slack
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/integrations/davis-assistant-for-microsoft-teams/" tabindex="-1">
      
          Microsoft Teams
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/davis-assistant/integrations/build-a-custom-davis-assistant-integration/" tabindex="-1">
      
          Custom integrations
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/" tabindex="-1">
      
          Problem detection and analysis
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/how-problems-are-detected-and-analyzed/" tabindex="-1">
      
          How problems are detected and analyzed
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/event-types/" tabindex="-1">
      
          Event types
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/event-types/availability-events/" tabindex="-1">
      
          Availability events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/event-types/custom-alerts/" tabindex="-1">
      
          Custom alerts
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/event-types/error-events/" tabindex="-1">
      
          Error events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/event-types/info-events/" tabindex="-1">
      
          Info events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/event-types/resource-events/" tabindex="-1">
      
          Resource events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/event-types/slowdown-events/" tabindex="-1">
      
          Slowdown events
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/problem-impact-level/" tabindex="-1">
      
          How Davis detects the impact of a problem
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/view-the-history-of-open-closed-problems/" tabindex="-1">
      
          View the history of open/closed problems
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/basic-concepts/problem-overview-page/" tabindex="-1">
      
          Problem overview page
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Problem detection
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-detection/automated-multi-dimensional-baselining/" tabindex="-1">
      
          Automated multi-dimensional baselining
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-detection/static-thresholds/" tabindex="-1">
      
          Static thresholds
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-detection/how-to-adjust-the-sensitivity-of-problem-detection/" tabindex="-1">
      
          How to adjust the sensitivity of problem detection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-detection/prediction-based-anomaly-detection/" tabindex="-1">
      
          Prediction-based anomaly detection
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-detection/detection-of-frequent-issues/" tabindex="-1">
      
          Detection of frequent issues
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-detection/metric-events-for-alerting/" tabindex="-1">
      
          Use custom metric events for alerting
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Problem analysis
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-analysis/impact-analysis/" tabindex="-1">
      
          Impact analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-analysis/root-cause-analysis/" tabindex="-1">
      
          Root cause analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-analysis/event-analytics/" tabindex="-1">
      
          Event analytics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/problem-analysis/percentiles-for-analyzing-performance/" tabindex="-1">
      
          Use percentiles to analyze application performance
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Notifications and alerting
      
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/notifications-and-alerting/maintenance-windows/" tabindex="-1">
      
          Maintenance windows
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/notifications-and-alerting/maintenance-windows/define-maintenance-window/" tabindex="-1">
      
          Define a maintenance window
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app/" tabindex="-1">
      
          Push notifications via the Dynatrace mobile app
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/problem-detection-and-analysis/notifications-and-alerting/how-can-i-filter-problem-notifications-with-alerting-profiles/" tabindex="-1">
      
          Filter problem notifications with alerting profiles
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/diagnostics/" tabindex="-1">
      
          Diagnostics
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/cpu-analysis/" tabindex="-1">
      
          CPU analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/crash-analysis/" tabindex="-1">
      
          Crash analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/exception-analysis/" tabindex="-1">
      
          Exception analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/memory-dump-analysis/" tabindex="-1">
      
          Memory dump analysis
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/top-database-statements/" tabindex="-1">
      
          Top database statements
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/diagnostics/top-web-requests/" tabindex="-1">
      
          Top web requests
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/smartscape/" tabindex="-1">
      
          Smartscape
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/smartscape/visualize-your-environment-topology-through-smartscape/" tabindex="-1">
      
          Visualize your environment topology through Smartscape
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/tags-and-metadata/" tabindex="-1">
      
          Tags and metadata
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basic concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/tags-and-metadata/basic-concepts/tags-vs-metadata/" tabindex="-1">
      
          Tags vs metadata
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging/" tabindex="-1">
      
          Best practices and recommendations for tagging
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Reference
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/tags-and-metadata/reference/regular-expressions-in-dynatrace/" tabindex="-1">
      
          Regular expressions in Dynatrace
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Setup
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/tags-and-metadata/setup/how-to-define-tags/" tabindex="-1">
      
          How to define tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/tags-and-metadata/setup/define-tags-based-on-environment-variables/" tabindex="-1">
      
          Define tags based on environment variables
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Use cases
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/cloud-foundry/other-deployments-and-configurations/leverage-tags-defined-in-cloud-foundry-deployments/" tabindex="-1">
      
          Organize Cloud Foundry deployments by tags
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/openshift/other-deployments-and-configurations/leverage-tags-defined-in-openshift-deployments/" tabindex="-1">
      
          Organize OpenShift deployments by tags
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/hosts/configuration/define-tags-and-metadata-for-hosts/" tabindex="-1">
      
          Define tags and metadata for hosts
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/technology-support/cloud-platforms/kubernetes/other-deployments-and-configurations/leverage-tags-defined-in-kubernetes-deployments/" tabindex="-1">
      
          Organize Kubernetes deployments by tags
      
          </a>
        </span>
      </li><li class=" is-reference">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/process-groups/configuration/define-your-own-process-group-metadata/" tabindex="-1">
      
          Define your own process group metadata
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/management-zones/" tabindex="-1">
      
          Management zones
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/management-zones/set-up-management-zones/" tabindex="-1">
      
          Set up management zones
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/management-zones/how-to-use-management-zones/" tabindex="-1">
      
          How to use management zones
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/" tabindex="-1">
      
          User management and SSO
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-groups-and-permissions/" tabindex="-1">
      
          Manage user groups and permissions
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-saml/" tabindex="-1">
      
          Manage users and groups with SAML in Dynatrace SaaS
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-saml/saml-ad-fs/" tabindex="-1">
      
          AD FS SAML configuration for Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-saml/saml-azure/" tabindex="-1">
      
          Azure SAML configuration for Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-saml/saml-gsuite/" tabindex="-1">
      
          GSuite (Google) SAML configuration for Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-saml/saml-okta/" tabindex="-1">
      
          Okta SAML configuration for Dynatrace
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-scim/" tabindex="-1">
      
          Manage users and groups with SCIM in Dynatrace SaaS
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-scim/scim-azure/" tabindex="-1">
      
          Azure SCIM configuration for Dynatrace
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/how-to-use-dynatrace/user-management-and-sso/manage-users-and-groups-with-scim/scim-okta/" tabindex="-1">
      
          Okta SCIM configuration for Dynatrace
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children  is-active" role="treeitem" aria-expanded="true" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/" tabindex="-1">
      
          Dynatrace API
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Basics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/basics/dynatrace-api-authentication/" tabindex="-1">
      
          Authentication
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/basics/dynatrace-api-response-codes/" tabindex="-1">
      
          Response codes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/basics/access-limit/" tabindex="-1">
      
          Access limit
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/basics/preview-early-access/" tabindex="-1">
      
          Preview and Early Adopter releases
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children  is-active" role="treeitem" aria-expanded="true" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/" tabindex="-1">
      
          Environment API
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/activegates/" tabindex="-1">
      
          ActiveGates
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/activegates/get-all/" tabindex="-1">
      
          GET all ActiveGates
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/activegates/get-activegate/" tabindex="-1">
      
          GET an ActiveGate
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Auto update jobs
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/activegates/auto-update-jobs/get-all-jobs/" tabindex="-1">
      
          GET all auto-update jobs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/activegates/auto-update-jobs/get-job/" tabindex="-1">
      
          GET an auto-update job
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/activegates/auto-update-jobs/post-job/" tabindex="-1">
      
          POST an auto-update job
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/activegates/auto-update-jobs/delete-job/" tabindex="-1">
      
          DELETE an auto-update job
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/activegates/auto-update-jobs/get-activegates-jobs/" tabindex="-1">
      
          GET ActiveGates with auto-update jobs
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/anonymization/" tabindex="-1">
      
          Anonymization
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/anonymization/put-job/" tabindex="-1">
      
          PUT anonymization job
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/anonymization/get-job-status/" tabindex="-1">
      
          GET job status
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/audit-logs/" tabindex="-1">
      
          Audit logs
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/audit-logs/get-log/" tabindex="-1">
      
          GET audit log
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/audit-logs/get-entry/" tabindex="-1">
      
          GET audit log entry
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/cluster-information/" tabindex="-1">
      
          Cluster information
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/custom-tags/" tabindex="-1">
      
          Custom tags
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/custom-tags/get-tags/" tabindex="-1">
      
          GET tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/custom-tags/post-tags/" tabindex="-1">
      
          POST tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/custom-tags/del-tags/" tabindex="-1">
      
          DELETE tags
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/deployment/" tabindex="-1">
      
          Deployment
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          OneAgent
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest/" tabindex="-1">
      
          Download latest OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version/" tabindex="-1">
      
          Download OneAgent of specific version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/oneagent/get-available-versions/" tabindex="-1">
      
          GET available versions of OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/oneagent/get-version-latest/" tabindex="-1">
      
          GET the latest version of OneAgent
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info/" tabindex="-1">
      
          GET OneAgent connectivity info
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info-endpoints/" tabindex="-1">
      
          GET ActiveGate endpoints for OneAgent
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          ActiveGate
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/activegate/download-activegate-latest/" tabindex="-1">
      
          Download latest ActiveGate
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/activegate/download-activegate-version/" tabindex="-1">
      
          Download ActiveGate of specific version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions/" tabindex="-1">
      
          GET available versions of ActiveGate
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Bosh
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/bosh/download-bosh-version/" tabindex="-1">
      
          Download BOSH tarballs of specific version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/bosh/get-available-version/" tabindex="-1">
      
          GET available versions of BOSH tarballs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/deployment/bosh/get-bosh-checksum/" tabindex="-1">
      
          GET checksum of a BOSH tarball
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/events/" tabindex="-1">
      
          Events
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/events/get-events-feed/" tabindex="-1">
      
          GET feed
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/events/get-event/" tabindex="-1">
      
          GET an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/events/post-event/" tabindex="-1">
      
          POST an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/events/push-deployment-events-from-jenkins/" tabindex="-1">
      
          Push deployment events from Jenkins
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/" tabindex="-1">
      
          Log Monitoring
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/" tabindex="-1">
      
          Host logs
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/get-logs/" tabindex="-1">
      
          GET logs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/post-analysis-job/" tabindex="-1">
      
          POST analysis job
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/get-analysis-job-status/" tabindex="-1">
      
          GET analysis job status
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/get-log-content/" tabindex="-1">
      
          GET log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/post-log-content/" tabindex="-1">
      
          POST filtered log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/post-top-log-content/" tabindex="-1">
      
          POST top log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/hosts/del-analysis-job/" tabindex="-1">
      
          DELETE analysis job
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/" tabindex="-1">
      
          Process groups logs
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/get-logs/" tabindex="-1">
      
          GET logs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/post-analysis-job/" tabindex="-1">
      
          POST analysis job
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/get-analysis-job-status/" tabindex="-1">
      
          GET analysis job status
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/get-log-content/" tabindex="-1">
      
          GET log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/post-log-content/" tabindex="-1">
      
          POST filtered log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/post-top-log-content/" tabindex="-1">
      
          POST top log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/process-groups/del-analysis-job/" tabindex="-1">
      
          DELETE analysis job
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/" tabindex="-1">
      
          Custom devices logs
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/get-logs/" tabindex="-1">
      
          GET logs
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/post-analysis-job/" tabindex="-1">
      
          POST analysis job
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/get-analysis-job-status/" tabindex="-1">
      
          GET analysis job status
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/get-log-content/" tabindex="-1">
      
          GET log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/post-log-content/" tabindex="-1">
      
          POST filtered log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/post-top-log-content/" tabindex="-1">
      
          POST top log content
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/log-monitoring/custom-device/del-analysis-job/" tabindex="-1">
      
          DELETE analysis job
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/" tabindex="-1">
      
          Timeseries v1
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Metric definitions
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/metric-definitions/get-list/" tabindex="-1">
      
          GET list of metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/metric-definitions/get-definition/" tabindex="-1">
      
          GET definition of a metric
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Read data points
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/read-data-points/get-data-points/" tabindex="-1">
      
          GET data points
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/read-data-points/post-data-points/" tabindex="-1">
      
          POST data points
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/custom-metrics/" tabindex="-1">
      
          Custom metrics
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/custom-metrics/put-custom-metric/" tabindex="-1">
      
          PUT a custom metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/custom-metrics/delete-custom-metric/" tabindex="-1">
      
          DELETE a custom metric
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Available metrics
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/available-metrics/saas/" tabindex="-1">
      
          SaaS
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v1/available-metrics/managed/" tabindex="-1">
      
          Managed
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children  is-active" role="treeitem" aria-expanded="true" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/" tabindex="-1">
      
          Metrics v2
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="is-active" aria-expanded="true">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/" tabindex="-1">
      
          GET metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/get-descriptor/" tabindex="-1">
      
          GET metric descriptor
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/get-data-points/" tabindex="-1">
      
          GET metric data points
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/selector-transformations/" tabindex="-1">
      
          Selector transformation
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/examples/" tabindex="-1">
      
          Examples and use cases
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/examples/list-all-metrics/" tabindex="-1">
      
          List all metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/examples/select-multiple-metrics/" tabindex="-1">
      
          Select multiple metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/metric-v2/examples/select-subtree/" tabindex="-1">
      
          Select full metric subtree
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/network-zones/" tabindex="-1">
      
          Network zones
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/network-zones/get-all/" tabindex="-1">
      
          GET all network zones
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/network-zones/get-network-zone/" tabindex="-1">
      
          GET a network zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/network-zones/put-network-zone/" tabindex="-1">
      
          PUT a network zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/network-zones/del-network-zone/" tabindex="-1">
      
          DELETE a network zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/network-zones/get-global-config/" tabindex="-1">
      
          GET global configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/network-zones/put-global-config/" tabindex="-1">
      
          PUT global configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/oneagent-on-host/" tabindex="-1">
      
          OneAgent on a host
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/" tabindex="-1">
      
          Topology and Smartscape v1
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/applications-api/" tabindex="-1">
      
          Applications
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all/" tabindex="-1">
      
          GET all apps
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app/" tabindex="-1">
      
          GET an app
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags/" tabindex="-1">
      
          POST tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline/" tabindex="-1">
      
          GET baseline
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/" tabindex="-1">
      
          Hosts
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all/" tabindex="-1">
      
          GET all hosts
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host/" tabindex="-1">
      
          GET a host
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags/" tabindex="-1">
      
          POST tags
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/processes-api/" tabindex="-1">
      
          Processes
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all/" tabindex="-1">
      
          GET all processes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process/" tabindex="-1">
      
          GET a process
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/" tabindex="-1">
      
          Process groups
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all/" tabindex="-1">
      
          GET all process groups
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group/" tabindex="-1">
      
          GET a process group
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags/" tabindex="-1">
      
          POST tags
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/services-api/" tabindex="-1">
      
          Services
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all/" tabindex="-1">
      
          GET all services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service/" tabindex="-1">
      
          GET a service
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags/" tabindex="-1">
      
          POST tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline/" tabindex="-1">
      
          GET baseline
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/" tabindex="-1">
      
          Custom device
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api/" tabindex="-1">
      
          Create custom device
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api/" tabindex="-1">
      
          Report custom device metric
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/entity-v2/" tabindex="-1">
      
          Monitored entities v2
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/entity-v2/get-entities-list/" tabindex="-1">
      
          GET entities list
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/entity-v2/get-entity/" tabindex="-1">
      
          GET an entity
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/entity-v2/get-all-entity-types/" tabindex="-1">
      
          GET all entity types
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/entity-v2/get-entity-type/" tabindex="-1">
      
          GET entity type
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/entity-v2/post-custom-device/" tabindex="-1">
      
          POST a custom device
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/problems/" tabindex="-1">
      
          Problems
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Problems
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/problems/get-status/" tabindex="-1">
      
          GET count
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/problems/get-feed/" tabindex="-1">
      
          GET feed
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/problems/get-details/" tabindex="-1">
      
          GET details
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/problems/get-close/" tabindex="-1">
      
          GET close
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/problems/post-close/" tabindex="-1">
      
          POST close
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Comments
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/comments/get-all/" tabindex="-1">
      
          GET all
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/comments/post-comment/" tabindex="-1">
      
          POST a comment
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/comments/put-comment/" tabindex="-1">
      
          PUT a comment
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/problems/comments/del-comment/" tabindex="-1">
      
          DELETE a comment
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/" tabindex="-1">
      
          Real User Monitoring JavaScript code
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-list-injected-applications/" tabindex="-1">
      
          GET list of injected applications
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-most-recent-version/" tabindex="-1">
      
          GET latest version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-current-version/" tabindex="-1">
      
          GET current version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-javascript-tag/" tabindex="-1">
      
          GET JavaScript tag
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-oneagent-javascript-tag/" tabindex="-1">
      
          GET OneAgent JavaScript tag
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-snippet-sync/" tabindex="-1">
      
          GET sync code snippet
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-snippet-async/" tabindex="-1">
      
          GET async code snippet
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-javascript-code/get-inline/" tabindex="-1">
      
          GET inline code
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/real-user-monitoring-browser-extension/" tabindex="-1">
      
          Real User Monitoring browser extension
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/synthetic/" tabindex="-1">
      
          Synthetic
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-monitors/" tabindex="-1">
      
          Synthetic monitors
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-all-monitors/" tabindex="-1">
      
          GET all monitors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-a-monitor/" tabindex="-1">
      
          GET a monitor
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-monitors/post-a-monitor/" tabindex="-1">
      
          POST a monitor
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-monitors/put-a-monitor/" tabindex="-1">
      
          PUT a monitor
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-monitors/delete-a-monitor/" tabindex="-1">
      
          DELETE a monitor
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-monitors/models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-locations/" tabindex="-1">
      
          Synthetic locations
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations/" tabindex="-1">
      
          GET all locations
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-locations/get-a-location/" tabindex="-1">
      
          GET a location
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-locations/post-a-location/" tabindex="-1">
      
          POST a location
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-locations/put-a-location/" tabindex="-1">
      
          PUT a location
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-locations/delete-a-location/" tabindex="-1">
      
          DELETE a location
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-nodes/" tabindex="-1">
      
          Synthetic nodes
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all/" tabindex="-1">
      
          GET all
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-node/" tabindex="-1">
      
          GET a node
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/synthetic/third-party-synthetic/" tabindex="-1">
      
          Third-party synthetic
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-monitors/" tabindex="-1">
      
          POST third-party monitors
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-events/" tabindex="-1">
      
          POST third-party events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-modify-state/" tabindex="-1">
      
          POST modify state of third-party monitors
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/tokens/" tabindex="-1">
      
          Tokens
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/get-all-tokens/" tabindex="-1">
      
          GET all tokens
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/post-new-token/" tabindex="-1">
      
          POST a new token
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/get-token-metadata/" tabindex="-1">
      
          GET token metadata
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/post-token-metadata/" tabindex="-1">
      
          POST token lookup
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/put-token/" tabindex="-1">
      
          PUT an existing token
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/delete-token/" tabindex="-1">
      
          DELETE an existing token
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/delete-exposed-token/" tabindex="-1">
      
          Find and replace an exposed token
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/tokens/token-rotation/" tabindex="-1">
      
          Token rotation
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/environment-api/user-sessions/" tabindex="-1">
      
          User sessions
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/user-sessions/table/" tabindex="-1">
      
          GET table
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/environment-api/user-sessions/tree/" tabindex="-1">
      
          GET tree
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/" tabindex="-1">
      
          Configuration API
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/alerting-profiles-api/" tabindex="-1">
      
          Alerting profiles
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/alerting-profiles-api/get-all/" tabindex="-1">
      
          GET all profiles
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/alerting-profiles-api/get-profile/" tabindex="-1">
      
          GET a profile
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/alerting-profiles-api/post-profile/" tabindex="-1">
      
          POST a profile
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/alerting-profiles-api/put-profile/" tabindex="-1">
      
          PUT a profile
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/alerting-profiles-api/del-profile/" tabindex="-1">
      
          DELETE a profile
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/" tabindex="-1">
      
          Anomaly detection
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/" tabindex="-1">
      
          Application
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/get-config/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/put-config/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/" tabindex="-1">
      
          AWS
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/get-config/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/put-config/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/" tabindex="-1">
      
          Database services
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/put-config/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/" tabindex="-1">
      
          Disk events
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/get-all/" tabindex="-1">
      
          GET all events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/get-event/" tabindex="-1">
      
          GET an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/post-event/" tabindex="-1">
      
          POST an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/put-event/" tabindex="-1">
      
          PUT an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/del-event/" tabindex="-1">
      
          DELETE an event
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/" tabindex="-1">
      
          Hosts
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/get-config/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/put-config/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/" tabindex="-1">
      
          Metric events
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/get-all/" tabindex="-1">
      
          GET all events
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/get-event/" tabindex="-1">
      
          GET an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/post-event/" tabindex="-1">
      
          POST an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/put-event/" tabindex="-1">
      
          PUT an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/del-event/" tabindex="-1">
      
          DELETE an event
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/json-models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/" tabindex="-1">
      
          Process groups
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/put-config/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/del-config/" tabindex="-1">
      
          DELETE configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services/" tabindex="-1">
      
          Services
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services/get-config/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services/put-config/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/" tabindex="-1">
      
          VMware
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/get-config/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/put-config/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/application-detection-configuration/" tabindex="-1">
      
          Applications detection
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/application-detection-configuration/get-all/" tabindex="-1">
      
          GET all rules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/application-detection-configuration/get-rule/" tabindex="-1">
      
          GET a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/application-detection-configuration/post-rule/" tabindex="-1">
      
          POST a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/application-detection-configuration/put-rule/" tabindex="-1">
      
          PUT a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/application-detection-configuration/del-rule/" tabindex="-1">
      
          DELETE a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/application-detection-configuration/reorder-rules/" tabindex="-1">
      
          PUT reorder rules
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/automatically-applied-tags-api/" tabindex="-1">
      
          Auto-tags
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/automatically-applied-tags-api/get-all/" tabindex="-1">
      
          GET all auto-tags
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/automatically-applied-tags-api/get-auto-tag/" tabindex="-1">
      
          GET an auto-tag
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/automatically-applied-tags-api/post-auto-tag/" tabindex="-1">
      
          POST an auto-tag
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/automatically-applied-tags-api/put-auto-tag/" tabindex="-1">
      
          PUT an auto-tag
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/automatically-applied-tags-api/del-auto-tag/" tabindex="-1">
      
          DELETE an auto-tag
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/automatically-applied-tags-api/models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/aws-credentials-api/" tabindex="-1">
      
          AWS credentials
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/aws-credentials-api/get-all/" tabindex="-1">
      
          GET all credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/aws-credentials-api/post-new-credentials/" tabindex="-1">
      
          POST new credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/aws-credentials-api/get-credentials/" tabindex="-1">
      
          GET credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/aws-credentials-api/put-credentials/" tabindex="-1">
      
          PUT credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/aws-credentials-api/delete-credentials/" tabindex="-1">
      
          DELETE credentials
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/azure-credentials-api/" tabindex="-1">
      
          Azure credentials
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/azure-credentials-api/get-all/" tabindex="-1">
      
          GET all credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/azure-credentials-api/get-credentials/" tabindex="-1">
      
          GET credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/azure-credentials-api/post-new-credentials/" tabindex="-1">
      
          POST new credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/azure-credentials-api/put-credentials/" tabindex="-1">
      
          PUT credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/azure-credentials-api/delete-credentials/" tabindex="-1">
      
          DELETE credentials
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/" tabindex="-1">
      
          Calculated metrics
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/log-monitoring-metrics-api/" tabindex="-1">
      
          Log Monitoring metrics
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/log-monitoring-metrics-api/get-all/" tabindex="-1">
      
          GET all metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/log-monitoring-metrics-api/get-metric/" tabindex="-1">
      
          GET a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/log-monitoring-metrics-api/put-metric/" tabindex="-1">
      
          PUT a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/log-monitoring-metrics-api/del-metric/" tabindex="-1">
      
          DELETE a metric
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/" tabindex="-1">
      
          Mobile apps metrics
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/get-all/" tabindex="-1">
      
          GET all metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/get-metric/" tabindex="-1">
      
          GET a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/post-metric/" tabindex="-1">
      
          POST a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/put-metric/" tabindex="-1">
      
          PUT a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/del-metric/" tabindex="-1">
      
          DELETE a metric
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/" tabindex="-1">
      
          RUM metrics
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/get-all/" tabindex="-1">
      
          GET all metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/get-metric/" tabindex="-1">
      
          GET a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/post-metric/" tabindex="-1">
      
          POST a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/put-metric/" tabindex="-1">
      
          PUT a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/del-metric/" tabindex="-1">
      
          DELETE a metric
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/" tabindex="-1">
      
          Synthetic metrics
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/get-all/" tabindex="-1">
      
          GET all metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/get-metric/" tabindex="-1">
      
          GET a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/post-metric/" tabindex="-1">
      
          POST a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/put-metric/" tabindex="-1">
      
          PUT a metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/del-metric/" tabindex="-1">
      
          DELETE a metric
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/cloud-foundry-foundations-credentials-api/" tabindex="-1">
      
          Cloud Foundry foundations credentials
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/cloud-foundry-foundations-credentials-api/get-all/" tabindex="-1">
      
          GET all credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/cloud-foundry-foundations-credentials-api/get-credentials/" tabindex="-1">
      
          GET credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/cloud-foundry-foundations-credentials-api/post-credentials/" tabindex="-1">
      
          POST credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/cloud-foundry-foundations-credentials-api/put-credentials/" tabindex="-1">
      
          PUT credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/cloud-foundry-foundations-credentials-api/delete-credentials/" tabindex="-1">
      
          DELETE credentials
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/conditional-naming/" tabindex="-1">
      
          Conditional naming
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/conditional-naming/get-all/" tabindex="-1">
      
          GET all rules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/conditional-naming/get-rule/" tabindex="-1">
      
          GET a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/conditional-naming/post-rule/" tabindex="-1">
      
          POST a new rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/conditional-naming/put-rule/" tabindex="-1">
      
          PUT a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/conditional-naming/del-rule/" tabindex="-1">
      
          DELETE a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/conditional-naming/json-models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/credential-vault/" tabindex="-1">
      
          Credential vault
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/credential-vault/get-all/" tabindex="-1">
      
          GET all credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/credential-vault/get-credentials/" tabindex="-1">
      
          GET credentials metadata
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/credential-vault/post-credentials/" tabindex="-1">
      
          POST a set of credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/credential-vault/put-credentials/" tabindex="-1">
      
          PUT a set of credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/credential-vault/del-credentials/" tabindex="-1">
      
          DELETE a set of credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/credential-vault/models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/dashboards-api/" tabindex="-1">
      
          Dashboards
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/dashboards-api/get-all/" tabindex="-1">
      
          GET all dashboards
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/dashboards-api/get-dashboard/" tabindex="-1">
      
          GET a dashboard
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/dashboards-api/post-dashboard/" tabindex="-1">
      
          POST a dashboard
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/dashboards-api/put-dashboard/" tabindex="-1">
      
          PUT a dashboard
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/dashboards-api/del-dahsboard/" tabindex="-1">
      
          DELETE a dashboard
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models/" tabindex="-1">
      
          Tile JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/data-privacy-api/" tabindex="-1">
      
          Data privacy
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/data-privacy-api/get-configuration/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/data-privacy-api/put-configuration/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/" tabindex="-1">
      
          Extensions
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-all-extensions/" tabindex="-1">
      
          GET all extensions
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-an-extension/" tabindex="-1">
      
          GET an extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-state/" tabindex="-1">
      
          GET extension&apos;s states
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/post-an-extension/" tabindex="-1">
      
          POST an extension .zip file
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-extension-file/" tabindex="-1">
      
          GET extension .zip file
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/del-extension-file/" tabindex="-1">
      
          DELETE extension .zip file
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-all-instances/" tabindex="-1">
      
          GET all instances of an extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-an-instance/" tabindex="-1">
      
          GET an instance of an extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/post-instance/" tabindex="-1">
      
          POST a new instance of an extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/put-instance/" tabindex="-1">
      
          PUT an instance of an extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/del-instance/" tabindex="-1">
      
          DELETE an instance of an extension
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-global-configuration/" tabindex="-1">
      
          GET global configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/put-global-configuration/" tabindex="-1">
      
          PUT global configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-all-ag-modules/" tabindex="-1">
      
          GET all ActiveGate extension modules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/extensions-api/get-available-hosts/" tabindex="-1">
      
          GET all hosts
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/frequent-issue-detection-api/" tabindex="-1">
      
          Frequent issue detection
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/frequent-issue-detection-api/get-configuration/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/frequent-issue-detection-api/put-configuration/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/k8s-credentials-api-api/" tabindex="-1">
      
          Kubernetes credentials
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/k8s-credentials-api-api/get-all/" tabindex="-1">
      
          GET all credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/k8s-credentials-api-api/get-credentials/" tabindex="-1">
      
          GET credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/k8s-credentials-api-api/post-new-credentials/" tabindex="-1">
      
          POST new credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/k8s-credentials-api-api/put-credentials/" tabindex="-1">
      
          PUT credentials
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/k8s-credentials-api-api/delete-credentials/" tabindex="-1">
      
          DELETE credentials
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/maintenance-windows-api/" tabindex="-1">
      
          Maintenance windows
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/maintenance-windows-api/get-all/" tabindex="-1">
      
          GET all maintenance windows
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/maintenance-windows-api/get-mw/" tabindex="-1">
      
          GET a maintenance window
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/maintenance-windows-api/post-mw/" tabindex="-1">
      
          POST a maintenance window
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/maintenance-windows-api/put-mw/" tabindex="-1">
      
          PUT a maintenance window
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/maintenance-windows-api/delete-mw/" tabindex="-1">
      
          DELETE a maintenance window
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/" tabindex="-1">
      
          Management zones
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/get-all/" tabindex="-1">
      
          GET all management zones
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/get-mz/" tabindex="-1">
      
          GET a management zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/post-mz/" tabindex="-1">
      
          POST a management zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/put-mz/" tabindex="-1">
      
          PUT a management zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/del-mz/" tabindex="-1">
      
          DELETE a management zone
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/json-models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/management-zones-api/copy-management-zones-between-dynatrace-environments/" tabindex="-1">
      
          Copy management zones between Dynatrace environments
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/" tabindex="-1">
      
          Mobile Symbolication
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/get-all/" tabindex="-1">
      
          GET all
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/get-storage-info/" tabindex="-1">
      
          GET storage info
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/get-supported-versions/" tabindex="-1">
      
          GET supported version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app/" tabindex="-1">
      
          GET files for an app
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version/" tabindex="-1">
      
          PUT files for an app
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/del-files-app/" tabindex="-1">
      
          DELETE files for an app
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app-version/" tabindex="-1">
      
          GET files for an app version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/del-files-app-version/" tabindex="-1">
      
          DELETE files for an app version
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version-pin/" tabindex="-1">
      
          PUT pin files
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/notifications-api/" tabindex="-1">
      
          Notifications
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/notifications-api/get-all-notifications/" tabindex="-1">
      
          GET all notifications
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/notifications-api/get-a-notification/" tabindex="-1">
      
          GET a notification
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/notifications-api/post-a-notification/" tabindex="-1">
      
          POST a notification configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/notifications-api/put-a-notification/" tabindex="-1">
      
          PUT a notification configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/notifications-api/delete-a-notification/" tabindex="-1">
      
          DELETE a notification
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/notifications-api/models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/" tabindex="-1">
      
          OneAgent on a host
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-config/" tabindex="-1">
      
          OneAgent configuration
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-auto-update/" tabindex="-1">
      
          Auto-update configuration
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-auto-update/get-auto-update-configuration/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-monitoring/" tabindex="-1">
      
          Monitoring configuration
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-monitoring/get-monitoring-configuration/" tabindex="-1">
      
          GET configuration
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration/" tabindex="-1">
      
          PUT configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/oneagent-on-host/oneagent-technology-monitoring/" tabindex="-1">
      
          Technology monitoring configuration
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/" tabindex="-1">
      
          Plugins
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/get-all-plugins/" tabindex="-1">
      
          GET all plugins
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/get-a-plugin/" tabindex="-1">
      
          GET a plugin
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/get-a-plugin-state/" tabindex="-1">
      
          GET states of a plugin
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/post-a-plugin/" tabindex="-1">
      
          POST a plugin ZIP file
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/get-plugin-binary/" tabindex="-1">
      
          GET plugin ZIP file
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/delete-plugin-binary/" tabindex="-1">
      
          DELETE plugin ZIP file
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/get-all-endpoints/" tabindex="-1">
      
          GET all plugin&apos;s endpoints
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/get-an-endpoint/" tabindex="-1">
      
          GET a plugin&apos;s endpoint
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/post-an-endpoint/" tabindex="-1">
      
          POST a new plugin&apos;s endpoint
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/put-an-endpoint/" tabindex="-1">
      
          PUT an endpoint of a plugin
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/delete-an-endpoint/" tabindex="-1">
      
          DELETE a plugin&apos;s endpoint
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/plugins-api/get-all-ag-modules/" tabindex="-1">
      
          GET all ActiveGate plugin modules
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/remote-environments/" tabindex="-1">
      
          Remote environments
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/remote-environments/get-all/" tabindex="-1">
      
          GET all environments
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/remote-environments/get-remote-environment/" tabindex="-1">
      
          GET a remote environment
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/remote-environments/post-remote-environment/" tabindex="-1">
      
          POST a remote environment
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/remote-environments/put-remote-environment/" tabindex="-1">
      
          PUT a remote environment
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/remote-environments/del-remote-environment/" tabindex="-1">
      
          DELETE a remote environment
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/" tabindex="-1">
      
          Reports
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/get-all/" tabindex="-1">
      
          GET all reports
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/get-report/" tabindex="-1">
      
          GET a report
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/post-report/" tabindex="-1">
      
          POST a report
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/put-report/" tabindex="-1">
      
          PUT a report
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/del-report/" tabindex="-1">
      
          DELETE a report
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/subscribe-report/" tabindex="-1">
      
          POST subscribe
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/reports-api/unsubscribe-report/" tabindex="-1">
      
          POST unsubscribe
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/service-api/" tabindex="-1">
      
          Services
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/service-api/calculated-metric/" tabindex="-1">
      
          Calculated metrics
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/calculated-metric/get-all/" tabindex="-1">
      
          GET all calculated metrics
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/calculated-metric/get-calculated-metric/" tabindex="-1">
      
          GET a calculated metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/calculated-metric/post-calculated-metric/" tabindex="-1">
      
          POST a calculated metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/calculated-metric/put-calculated-metric/" tabindex="-1">
      
          PUT a calculated metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/calculated-metric/del-calculated-metric/" tabindex="-1">
      
          DELETE a calculated metric
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/calculated-metric/json-models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/service-api/custom-services-api/" tabindex="-1">
      
          Custom services
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/custom-services-api/get-all/" tabindex="-1">
      
          GET all custom services
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/custom-services-api/get-rule/" tabindex="-1">
      
          GET a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/custom-services-api/post-rule/" tabindex="-1">
      
          POST a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/custom-services-api/put-rule/" tabindex="-1">
      
          PUT a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/custom-services-api/del-rule/" tabindex="-1">
      
          DELETE a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/custom-services-api/reorder-rules/" tabindex="-1">
      
          PUT reorder rules
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/" tabindex="-1">
      
          Detection rules
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Full web request
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-all/" tabindex="-1">
      
          GET all rules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-a-rule/" tabindex="-1">
      
          GET a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/post-a-rule/" tabindex="-1">
      
          POST a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/put-a-rule/" tabindex="-1">
      
          PUT a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/del-a-rule/" tabindex="-1">
      
          DELETE a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/reorder-rules/" tabindex="-1">
      
          PUT reorder rules
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Opaque web request
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-all/" tabindex="-1">
      
          GET all rules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-a-rule/" tabindex="-1">
      
          GET a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/post-a-rule/" tabindex="-1">
      
          POST a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/put-a-rule/" tabindex="-1">
      
          PUT a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/del-a-rule/" tabindex="-1">
      
          DELETE a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/reorder-rules/" tabindex="-1">
      
          PUT reorder rules
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Full web service
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-all/" tabindex="-1">
      
          GET all rules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-a-rule/" tabindex="-1">
      
          GET a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/post-a-rule/" tabindex="-1">
      
          POST a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/put-a-rule/" tabindex="-1">
      
          PUT a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/del-a-rule/" tabindex="-1">
      
          DELETE a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/reorder-rules/" tabindex="-1">
      
          PUT reorder rules
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/detection-rules/models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/" tabindex="-1">
      
          IBM MQ tracing
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Queue managers
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queue-managers/get-queue-manager-all/" tabindex="-1">
      
          GET all queue managers
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queue-managers/get-queue-manager/" tabindex="-1">
      
          GET a queue manager
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queue-managers/put-queue-manager/" tabindex="-1">
      
          PUT a queue manager
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queue-managers/delete-queue-manager/" tabindex="-1">
      
          DELETE a queue manager
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Queues
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queues/get-all-queues/" tabindex="-1">
      
          GET all queues
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queues/get-queue/" tabindex="-1">
      
          GET a queue
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queues/post-new-queue/" tabindex="-1">
      
          POST a new queue
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queues/put-queue/" tabindex="-1">
      
          PUT a queue
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/ibm-mq-tracing-api/queues/delete-queue/" tabindex="-1">
      
          DELETE a queue
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-attributes-api/" tabindex="-1">
      
          Request attributes
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-attributes-api/get-all/" tabindex="-1">
      
          GET all request attributes
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-attributes-api/get-request-attribute/" tabindex="-1">
      
          GET a request attribute
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-attributes-api/post-request-attribute/" tabindex="-1">
      
          POST a request attribute
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-attributes-api/put-request-attribute/" tabindex="-1">
      
          PUT a request attribute
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-attributes-api/del-request-attribute/" tabindex="-1">
      
          DELETE a request attribute
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/" tabindex="-1">
      
          Request naming
      
          </a>
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/get-all/" tabindex="-1">
      
          GET all rules
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/get-a-rule/" tabindex="-1">
      
          GET a rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule/" tabindex="-1">
      
          POST a new rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/put-a-rule/" tabindex="-1">
      
          PUT a request naming rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/delete-a-rule/" tabindex="-1">
      
          DELETE a request naming rule
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/json-models/" tabindex="-1">
      
          JSON models
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule/" tabindex="-1">
      
          Create a new rule
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/" tabindex="-1">
      
          Web application configuration
      
          </a>
        </span>
        <ul class="toc__menu " role="group">
          <li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Web application
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/web-application/get-all/" tabindex="-1">
      
          GET all web applications
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/web-application/get-web-application/" tabindex="-1">
      
          GET a web application
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/web-application/post-web-application/" tabindex="-1">
      
          POST a web application
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/web-application/put-web-application/" tabindex="-1">
      
          PUT a web application
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/web-application/del-web-application/" tabindex="-1">
      
          DELETE a web application
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Default application
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/default-application/get-configuration/" tabindex="-1">
      
          GET default application
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/default-application/put-configuration/" tabindex="-1">
      
          PUT default application
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Data privacy
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps/" tabindex="-1">
      
          GET data privacy of all web applications
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/data-privacy/get-data-privacy-web-app/" tabindex="-1">
      
          GET data privacy of a web application
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/data-privacy/put-data-privacy-web-app/" tabindex="-1">
      
          PUT data privacy of a web application
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/data-privacy/get-data-privacy-default-app/" tabindex="-1">
      
          GET data privacy of the default application
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/dynatrace-api/configuration-api/web-application-configuration-api/data-privacy/put-data-privacy-default-app/" tabindex="-1">
      
          PUT data privacy of the default application
      
          </a>
        </span>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li>
        </ul>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Reference
      
        </span>
        <ul class="toc__menu " role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/dynatrace-web-ui-requirements/" tabindex="-1">
      
          Web UI requirements
      
          </a>
        </span>
      </li><li class="has-children " role="treeitem" aria-expanded="false" tabindex="0">
        <span class="toc__menu__entry">
            <button class="toc__menu__expand" tabindex="-1"></button>
      
          Dynatrace concepts
      
        </span>
        <ul class="toc__menu is-leaf" role="group">
          <li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/dynatrace-concepts/what-is-a-monitoring-environment/" tabindex="-1">
      
          What is a monitoring environment?
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/dynatrace-concepts/environment-id/" tabindex="-1">
      
          Environment ID
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/dynatrace-concepts/access-tokens/" tabindex="-1">
      
          Access tokens
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/dynatrace-concepts/can-i-set-up-multiple-monitoring-environments/" tabindex="-1">
      
          Can I set up multiple monitoring environments?
      
          </a>
        </span>
      </li>
        </ul>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/glossary/" tabindex="-1">
      
          Dynatrace glossary
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/help-on-help/" tabindex="-1">
      
          About Dynatrace Help
      
          </a>
        </span>
      </li><li class=" ">
        <span class="toc__menu__entry">
          <a href="/support/help/reference/monitoring-consumption-calculation/" tabindex="-1">
      
          Calculate Dynatrace monitoring consumption
      
          </a>
        </span>
      </li>
        </ul>
      </li></ul>
      </nav>
      <article class="island island--connected cf" id="content">
        <div class="search__results js-search-outlet"></div>
  <header class="title">
    <h1 class="title__headline" id="metrics-api-get-metrics">Metrics API - GET metrics<span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all"></span></h1>
  </header>
  <div class="content">
  <div class="content--main">
    <p>Lists all available metrics.</p>
<p>You can limit the output by using the pagination:</p>
<ol class="list">
<li>Specify the number of results per page in the <strong>pageSize</strong> query parameter.</li>
<li>Then use the cursor from the <strong>nextPageKey</strong> field of the previous response in the <strong>nextPageKey</strong> query parameter to obtain subsequent pages.</li>
</ol>
<p>The request produces one of the following types of payload, depending on the value of the the <strong>Accept</strong> request header:</p>
<ul class="list">
<li><code>application/json</code></li>
<li><code>text/csv; header=present</code>&#x2014;a CSV table with header row</li>
<li><code>text/csv; header=absent</code>&#x2014;a CSV table without header row</li>
</ul>
<p>If no <strong>Accept</strong> header is provided with the request, an <code>application/json</code> payload is returned.</p>
<p>

<table class="table swagger__propertytable--urltype">
  <tbody>
    <tr>
      <td>GET</td>
      <td>
        <ul class="list">
          <li>
            <span class="tag">Managed</span> https://{your-domain}/e/{your-environment-id}/api/v2/metrics
          </li>
          <li>
            <span class="tag">SaaS</span> https://{your-environment-id}.live.dynatrace.com/api/v2/metrics
          </li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

      </p><h4 id="authentication">Authentication</h4>
      <p>To execute this request, you need the <strong>Access problem and event feed, metrics, and topology</strong> (<code>DataExport</code>) permission assigned to your API token. To learn how to obtain and use it, see <a href="https://www.dynatrace.com/support/help/shortlink/api-authentication">Authentication</a>.</p>  


<h2 id="parameters">Parameters
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#parameters">
      </span></h2>
<p><table class="table swagger__propertytable swagger__propertytable--parametertype">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Description</th>
      <th>In</th>
      <th>Required</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="swagger__propertydata--simple">nextPageKey</td>
      <td class="swagger__propertydata--simple">
          string
      </td>
      <td class="swagger__propertydata--description">
        <p>The cursor for the next page of results. You can find it in the <strong>nextPageKey</strong> field of the previous response.</p>
<p>The first page is always returned if you don&apos;t specify the <strong>nextPageKey</strong> query parameter.</p>
<p>When the <strong>nextPageKey</strong> is set to obtain subsequent pages, you must omit all other query parameters.</p>

      </td>
      <td>query</td>
      <td class="swagger__propertydata--required">
          <span class="swagger__propertyvalue--optional">optional</span>
      </td>
    </tr>
    <tr>
      <td class="swagger__propertydata--simple">pageSize</td>
      <td class="swagger__propertydata--simple">
          integer
      </td>
      <td class="swagger__propertydata--description">
        <p>The desired amount of primary entities in a single response payload.</p>
<p>The maximal allowed page size is 5000.</p>
<p>If not set, 100 is used.</p>
<p>If a value higher than 5000 is used, only 5000 results per page are returned.</p>

      </td>
      <td>query</td>
      <td class="swagger__propertydata--required">
          <span class="swagger__propertyvalue--optional">optional</span>
      </td>
    </tr>
    <tr>
      <td class="swagger__propertydata--simple">metricSelector</td>
      <td class="swagger__propertydata--simple">
          string
      </td>
      <td class="swagger__propertydata--description">
        <p>Selects metrics for the query by their keys.</p>
<p>You can specify multiple metric keys separated by commas (for example, <code>metrickey1,metrickey2</code>). To select multiple metrics belonging to the same parent, list the last part of the required metric keys in parentheses, separated by commas, while keeping the common part untouched. For example, to list the <code>builtin:host.cpu.idle</code> and <code>builtin:host.cpu.user</code> metric, write: <code>builtin:host.cpu.(idle,user)</code>.</p>
<p>You can select a full set of related metrics by using a trailing asterisk (<code>*</code>) wildcard. For example, <code>builtin:host.*</code> selects all host-based metrics and <code>builtin:*</code> selects all Dynatrace-provided metrics.</p>
<p>You can set additional transformation operators, separated by a colon (<code>:</code>). See the <a href="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-selector">Metrics API - selector transformations help page</a> for additional information on available result transformations.</p>
<p>The length of the string is limited to 1,000 characters.</p>
<p>To find metrics based on a search term, rather than metricID, use the <strong>text</strong> query parameter instead of this one.</p>

      </td>
      <td>query</td>
      <td class="swagger__propertydata--required">
          <span class="swagger__propertyvalue--optional">optional</span>
      </td>
    </tr>
    <tr>
      <td class="swagger__propertydata--simple">text</td>
      <td class="swagger__propertydata--simple">
          string
      </td>
      <td class="swagger__propertydata--description">
        <p>Metric registry search term. Only show metrics that contain the term in their ID, display name, or description. Use the <code>metricSelector</code> parameter instead of this one to select a complete metric hierarchy instead of doing a text-based search.</p>

      </td>
      <td>query</td>
      <td class="swagger__propertydata--required">
          <span class="swagger__propertyvalue--optional">optional</span>
      </td>
    </tr>
    <tr>
      <td class="swagger__propertydata--simple">fields</td>
      <td class="swagger__propertydata--simple">
          string
      </td>
      <td class="swagger__propertydata--description">
        <p>Defines the list of metric properties included in the response.</p>
<p><code>metricId</code> is <strong>always</strong> included in the result. The following additional properties are available:</p>
<ul class="list">
<li><code>displayName</code>: The name of the metric in the user interface. Enabled by default.</li>
<li><code>description</code>: A short description of the metric. Enabled by default.</li>
<li><code>unit</code>: The unit of the metric. Enabled by default.</li>
<li><code>aggregationTypes</code>: The list of allowed aggregations for the metric. Note that it may be different after a <a href="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-selector">transformation</a> is applied.</li>
<li><code>defaultAggregation</code>: The default aggregation of the metric. It is used when no aggregation is specified or the <code>:auto</code> transformation is set.</li>
<li><code>dimensionDefinitions</code>: The fine metric division (for example, process group and process ID for some process-related metric).</li>
<li><code>transformations</code>: A list of <a href="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-selector">transformations</a> that can be applied to the metric.</li>
<li><code>entityType</code>: A list of entity types supported by the metric.</li>
</ul>
<p>To add properties, list them with leading plus <code>+</code>. To exclude default properties, list them with leading minus <code>-</code>.</p>
<p>To specify several properties, join them with a comma (for example <code>fields=+aggregationTypes,-description</code>).</p>
<p>If you specify just one property, the response contains the metric key and the specified property.To return metric keys only, specify <code>metricId</code> here.</p>

      </td>
      <td>query</td>
      <td class="swagger__propertydata--required">
          <span class="swagger__propertyvalue--optional">optional</span>
      </td>
    </tr>
  </tbody>
</table>


</p>
<h2 id="response-format">Response format
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#response-format">
      </span></h2>
<p>

<div class="tabgroup js-tabgroup" id="tabgroup-79" data-tabgroupid="tabgroup-79">
<div class="tabs is-hidden">


<input class="tab__input" type="radio" data-target="response-parameters" id="tabgroup-79-response-parameters" name="tabgroup-79" checked="checked">
<label class="tab" for="tabgroup-79-response-parameters">Response parameters</label>


<input class="tab__input" type="radio" data-target="json-model" id="tabgroup-79-json-model" name="tabgroup-79">
<label class="tab" for="tabgroup-79-json-model">JSON model</label>

</div>
<div class="tabgroup__content">
<div class="tab__content" data-content="response-parameters" data-title="Response parameters">
      <h3 id="metrics-get-response-metricdescriptorcollection" class="swagger__schemaheader">The <strong class="swagger__schemaheadername">MetricDescriptorCollection</strong> object
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#metrics-get-response-metricdescriptorcollection">
      </span></h3>
      <p>A list of metrics along with their descriptors.</p>

      <table class="table swagger__propertytable swagger__propertytable--responsetype">
        <thead>
          <tr>
            <th>Element</th>
            <th>Type</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="swagger__propertydata--simple">nextPageKey</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The cursor for the next page of results. Has the value of <code>null</code> on the last page.</p>
<p>Use it in the <strong>nextPageKey</strong> query parameter to obtain subsequent pages of the result.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">totalCount</td>
            <td class="swagger__propertydata--simple">
                  integer
            </td>
            <td class="swagger__propertydata--description"><p>The estimated number of metrics in the result.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">metrics</td>
            <td class="swagger__propertydata--simple">
                  <a href="#metrics-get-response-metricdescriptor">MetricDescriptor</a>[]
            </td>
            <td class="swagger__propertydata--description"><p>A list of metric along with their descriptors</p>

            </td>
          </tr>
        </tbody>
      </table>
      <h3 id="metrics-get-response-metricdescriptor" class="swagger__schemaheader">The <strong class="swagger__schemaheadername">MetricDescriptor</strong> object
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#metrics-get-response-metricdescriptor">
      </span></h3>
      <p>The descriptor of a metric.</p>

      <table class="table swagger__propertytable swagger__propertytable--responsetype">
        <thead>
          <tr>
            <th>Element</th>
            <th>Type</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="swagger__propertydata--simple">dimensionDefinitions</td>
            <td class="swagger__propertydata--simple">
                  <a href="#metrics-get-response-metricdimensiondefinition">MetricDimensionDefinition</a>[]
            </td>
            <td class="swagger__propertydata--description"><p>The fine metric division (for example, process group and process ID for some process-related metric).</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">defaultAggregation</td>
            <td class="swagger__propertydata--simple">
                  <a href="#metrics-get-response-metricdefaultaggregation">MetricDefaultAggregation</a>
            </td>
            <td class="swagger__propertydata--description">
            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">aggregationTypes</td>
            <td class="swagger__propertydata--simple">
                  string[]
            </td>
            <td class="swagger__propertydata--description"><p>The list of allowed aggregations for this metric.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">metricId</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The fully qualified key of the metric.</p>
<p>If a transformation has been used it is reflected in the metric key.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">entityType</td>
            <td class="swagger__propertydata--simple">
                  string[]
            </td>
            <td class="swagger__propertydata--description"><p>List of admissible primary entity types for this metric. Can be used for the <code>type</code> predicate in the <code>entitySelector</code>.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">displayName</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The name of the metric in the user interface.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">description</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>A short description of the metric.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">unit</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The unit of the metric.</p>

                The  <strong class="swagger__schemaheadername">unit</strong> element <a href="#metrics-get-response-enum-d2gqmdozs4l4zprh9ctxoa">can hold these values</a>.
            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">transformations</td>
            <td class="swagger__propertydata--simple">
                  string[]
            </td>
            <td class="swagger__propertydata--description"><p>Transform operators that could be appended to the current transformation list. Must be enabled with the &quot;fields&quot; parameter on <code>/metrics</code> and is always present on <code>/metrics/{metricId}</code>.</p>

            </td>
          </tr>
        </tbody>
      </table>
      <h3 id="metrics-get-response-metricdefaultaggregation" class="swagger__schemaheader">The <strong class="swagger__schemaheadername">MetricDefaultAggregation</strong> object
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#metrics-get-response-metricdefaultaggregation">
      </span></h3>
      <p>The default aggregation of a metric.</p>

      <table class="table swagger__propertytable swagger__propertytable--responsetype">
        <thead>
          <tr>
            <th>Element</th>
            <th>Type</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="swagger__propertydata--simple">parameter</td>
            <td class="swagger__propertydata--simple">
                  number
            </td>
            <td class="swagger__propertydata--description"><p>The percentile to be delivered. Valid values are between <code>0</code> and <code>100</code>.</p>
<p>Applicable only to the <code>percentile</code> aggregation type.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">type</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The type of default aggregation.</p>

                The  <strong class="swagger__schemaheadername">type</strong> element <a href="#metrics-get-response-enum-megqekhlrmeyejbzxd0lzg">can hold these values</a>.
            </td>
          </tr>
        </tbody>
      </table>
      <h3 id="metrics-get-response-metricdimensiondefinition" class="swagger__schemaheader">The <strong class="swagger__schemaheadername">MetricDimensionDefinition</strong> object
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#metrics-get-response-metricdimensiondefinition">
      </span></h3>
      <p>The dimension of a metric.</p>

      <table class="table swagger__propertytable swagger__propertytable--responsetype">
        <thead>
          <tr>
            <th>Element</th>
            <th>Type</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="swagger__propertydata--simple">name</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The name of the dimension.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">key</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The key of the dimension.</p>
<p>It must be unique within the metric.</p>

            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">type</td>
            <td class="swagger__propertydata--simple">
                  string
            </td>
            <td class="swagger__propertydata--description"><p>The type of the dimension.</p>

                The  <strong class="swagger__schemaheadername">type</strong> element <a href="#metrics-get-response-enum-swvqcnzbml4oscb1zheta">can hold these values</a>.
            </td>
          </tr>
          <tr>
            <td class="swagger__propertydata--simple">index</td>
            <td class="swagger__propertydata--simple">
                  integer
            </td>
            <td class="swagger__propertydata--description"><p>The unique 0-based index of the dimension.</p>
<p>Appending transformations such as :names or :parents may change the indexes of dimensions. <code>null</code> is used for the dimensions of a metric with flexible dimensions, which can be referenced with their dimension key, but do not have an intrinsic order that could be used for the index.</p>

            </td>
          </tr>
        </tbody>
      </table>

</div>
<div class="tab__content is-hidden" data-content="json-model" data-title="JSON model">
  <pre>
    <code class="language-json hljs">
{
  <span class="hljs-attr">&quot;totalCount&quot;</span>: <span class="hljs-number">3</span>,
  <span class="hljs-attr">&quot;nextPageKey&quot;</span>: <span class="hljs-string">&quot;ABCDEFABCDEFABCDEF_&quot;</span>,
  <span class="hljs-attr">&quot;metrics&quot;</span>: [
    {
      <span class="hljs-attr">&quot;metricId&quot;</span>: <span class="hljs-string">&quot;builtin:host.cpu.idle&quot;</span>,
      <span class="hljs-attr">&quot;displayName&quot;</span>: <span class="hljs-string">&quot;CPU idle&quot;</span>,
      <span class="hljs-attr">&quot;description&quot;</span>: <span class="hljs-string">&quot;Percentage of CPU time not being utilized, per host.\n&quot;</span>,
      <span class="hljs-attr">&quot;unit&quot;</span>: <span class="hljs-string">&quot;Percent&quot;</span>,
      <span class="hljs-attr">&quot;aggregationTypes&quot;</span>: [
        <span class="hljs-string">&quot;auto&quot;</span>,
        <span class="hljs-string">&quot;avg&quot;</span>,
        <span class="hljs-string">&quot;max&quot;</span>,
        <span class="hljs-string">&quot;min&quot;</span>
      ],
      <span class="hljs-attr">&quot;transformations&quot;</span>: [
        <span class="hljs-string">&quot;filter&quot;</span>,
        <span class="hljs-string">&quot;fold&quot;</span>,
        <span class="hljs-string">&quot;merge&quot;</span>,
        <span class="hljs-string">&quot;names&quot;</span>,
        <span class="hljs-string">&quot;parents&quot;</span>
      ],
      <span class="hljs-attr">&quot;defaultAggregation&quot;</span>: {
        <span class="hljs-attr">&quot;type&quot;</span>: <span class="hljs-string">&quot;avg&quot;</span>
      },
      <span class="hljs-attr">&quot;dimensionDefinitions&quot;</span>: [
        {
          <span class="hljs-attr">&quot;name&quot;</span>: <span class="hljs-string">&quot;primary&quot;</span>,
          <span class="hljs-attr">&quot;type&quot;</span>: <span class="hljs-string">&quot;ENTITY&quot;</span>
        }
      ],
      <span class="hljs-attr">&quot;entityType&quot;</span>: [
        <span class="hljs-string">&quot;HOST&quot;</span>
      ]
    },
    {
      <span class="hljs-attr">&quot;metricId&quot;</span>: <span class="hljs-string">&quot;builtin:host.cpu.user&quot;</span>,
      <span class="hljs-attr">&quot;displayName&quot;</span>: <span class="hljs-string">&quot;CPU idle&quot;</span>,
      <span class="hljs-attr">&quot;description&quot;</span>: <span class="hljs-string">&quot;Percentage of CPU utilized in user space, per host.\n&quot;</span>,
      <span class="hljs-attr">&quot;unit&quot;</span>: <span class="hljs-string">&quot;Percent&quot;</span>,
      <span class="hljs-attr">&quot;aggregationTypes&quot;</span>: [
        <span class="hljs-string">&quot;auto&quot;</span>,
        <span class="hljs-string">&quot;avg&quot;</span>,
        <span class="hljs-string">&quot;max&quot;</span>,
        <span class="hljs-string">&quot;min&quot;</span>
      ],
      <span class="hljs-attr">&quot;transformations&quot;</span>: [
        <span class="hljs-string">&quot;filter&quot;</span>,
        <span class="hljs-string">&quot;fold&quot;</span>,
        <span class="hljs-string">&quot;merge&quot;</span>,
        <span class="hljs-string">&quot;names&quot;</span>,
        <span class="hljs-string">&quot;parents&quot;</span>
      ],
      <span class="hljs-attr">&quot;defaultAggregation&quot;</span>: {
        <span class="hljs-attr">&quot;type&quot;</span>: <span class="hljs-string">&quot;avg&quot;</span>
      },
      <span class="hljs-attr">&quot;dimensionDefinitions&quot;</span>: [
        {
          <span class="hljs-attr">&quot;name&quot;</span>: <span class="hljs-string">&quot;primary&quot;</span>,
          <span class="hljs-attr">&quot;type&quot;</span>: <span class="hljs-string">&quot;ENTITY&quot;</span>
        }
      ],
      <span class="hljs-attr">&quot;entityType&quot;</span>: [
        <span class="hljs-string">&quot;HOST&quot;</span>
      ]
    }
  ]
}
    </code>
  </pre>

</div>
</div>
</div>
</p><h3 id="possible-values">Possible values
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#possible-values">
      </span></h3>

<div class="swagger__enum" id="metrics-get-response-enum-hb2kmfkzcytqyncihtkosg">
<h4 id="possible-values-for-the-transformations-element-in-the-metricdescriptor-object">Possible values for the <strong class="swagger__schemaheadername">transformations</strong> element in the <strong class="swagger__schemaheadername">MetricDescriptor</strong> object:</h4>

<ul class="list list--condensed">
<li>filter</li>
<li>fold</li>
<li>limit</li>
<li>merge</li>
<li>names</li>
<li>parents</li>
<li>rate</li>
<li>splitBy</li>
</ul>
</div>

<div class="swagger__enum" id="metrics-get-response-enum-d2gqmdozs4l4zprh9ctxoa">
<h4 id="possible-values-for-the-unit-element-in-the-metricdescriptor-object">Possible values for the <strong class="swagger__schemaheadername">unit</strong> element in the <strong class="swagger__schemaheadername">MetricDescriptor</strong> object:</h4>

<ul class="list list--condensed">
<li>Bit</li>
<li>BitPerHour</li>
<li>BitPerMinute</li>
<li>BitPerSecond</li>
<li>Byte</li>
<li>BytePerHour</li>
<li>BytePerMinute</li>
<li>BytePerSecond</li>
<li>Cores</li>
<li>Count</li>
<li>Day</li>
<li>GibiByte</li>
<li>Giga</li>
<li>GigaByte</li>
<li>Hour</li>
<li>KibiByte</li>
<li>KibiBytePerHour</li>
<li>KibiBytePerMinute</li>
<li>KibiBytePerSecond</li>
<li>Kilo</li>
<li>KiloByte</li>
<li>KiloBytePerHour</li>
<li>KiloBytePerMinute</li>
<li>KiloBytePerSecond</li>
<li>MebiByte</li>
<li>MebiBytePerHour</li>
<li>MebiBytePerMinute</li>
<li>MebiBytePerSecond</li>
<li>Mega</li>
<li>MegaByte</li>
<li>MegaBytePerHour</li>
<li>MegaBytePerMinute</li>
<li>MegaBytePerSecond</li>
<li>MicroSecond</li>
<li>MilliCores</li>
<li>MilliSecond</li>
<li>MilliSecondPerMinute</li>
<li>Minute</li>
<li>Month</li>
<li>NanoSecond</li>
<li>NanoSecondPerMinute</li>
<li>NotApplicable</li>
<li>PerHour</li>
<li>PerMinute</li>
<li>PerSecond</li>
<li>Percent</li>
<li>Pixel</li>
<li>Promille</li>
<li>Ratio</li>
<li>Second</li>
<li>State</li>
<li>Unspecified</li>
<li>Week</li>
<li>Year</li>
</ul>
</div>

<div class="swagger__enum" id="metrics-get-response-enum-kwbchnkihm3b6tworcnv6q">
<h4 id="possible-values-for-the-aggregationtypes-element-in-the-metricdescriptor-object">Possible values for the <strong class="swagger__schemaheadername">aggregationTypes</strong> element in the <strong class="swagger__schemaheadername">MetricDescriptor</strong> object:</h4>

<ul class="list list--condensed">
<li>auto</li>
<li>avg</li>
<li>count</li>
<li>max</li>
<li>median</li>
<li>min</li>
<li>percentile</li>
<li>sum</li>
<li>value</li>
</ul>
</div>

<div class="swagger__enum" id="metrics-get-response-enum-megqekhlrmeyejbzxd0lzg">
<h4 id="possible-values-for-the-type-element-in-the-metricdefaultaggregation-object">Possible values for the <strong class="swagger__schemaheadername">type</strong> element in the <strong class="swagger__schemaheadername">MetricDefaultAggregation</strong> object:</h4>

<ul class="list list--condensed">
<li>auto</li>
<li>avg</li>
<li>count</li>
<li>max</li>
<li>median</li>
<li>min</li>
<li>percentile</li>
<li>sum</li>
<li>value</li>
</ul>
</div>

<div class="swagger__enum" id="metrics-get-response-enum-swvqcnzbml4oscb1zheta">
<h4 id="possible-values-for-the-type-element-in-the-metricdimensiondefinition-object">Possible values for the <strong class="swagger__schemaheadername">type</strong> element in the <strong class="swagger__schemaheadername">MetricDimensionDefinition</strong> object:</h4>

<ul class="list list--condensed">
<li>ENTITY</li>
<li>NUMBER</li>
<li>OTHER</li>
<li>STRING</li>
<li>VOID</li>
</ul>
</div>


<h2 id="example">Example
      <span class="shortlink-copy shortlink-copy-js" data-clipboard-text="https://www.dynatrace.com/support/help/shortlink/api-metrics-v2-get-all#example">
      </span></h2>
<p>In this example, the request queries all built-in metrics (<strong>metricSelector</strong> is set to <code>builtin:*</code>) available in the <strong>mySampleEnv</strong> environment. The following fields are included in the response:</p>
<ul class="list">
<li>metricId</li>
<li>unit</li>
<li>aggregationTypes</li>
</ul>
<p>To achieve that, the <strong>fields</strong> query parameter is set to <code>unit,aggregationTypes</code>.</p>
<p>The API token is passed in the <strong>Authorization</strong> header.</p>
<p>The response is in <code>application/json</code> format and is truncated to four entries.</p>
<h4 id="curl">Curl</h4>
<pre><code class="language-bash hljs">curl -L -X GET <span class="hljs-string">&apos;https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=unit,aggregationTypes&amp;metricSelector=builtin:*&apos;</span> \
-H <span class="hljs-string">&apos;Authorization: Api-Token abcdefjhij1234567890&apos;</span> \
-H <span class="hljs-string">&apos;Accept: application/json&apos;</span>
</code></pre>
<h4 id="request-url">Request URL</h4>
<pre><code class="language-http hljs">https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=unit,aggregationTypes&amp;metricSelector=builtin:*
</code></pre>
<h4 id="response-body">Response body</h4>
<pre><code class="language-json hljs">{
  <span class="hljs-attr">&quot;totalCount&quot;</span>: <span class="hljs-number">1808</span>,
  <span class="hljs-attr">&quot;nextPageKey&quot;</span>: <span class="hljs-string">&quot;___a7acX3q0AAAAGAQAJYnVpbHRpbjoqAQA&quot;</span>,
  <span class="hljs-attr">&quot;metrics&quot;</span>: [
    {
      <span class="hljs-attr">&quot;metricId&quot;</span>: <span class="hljs-string">&quot;builtin:host.cpu.idle&quot;</span>,
      <span class="hljs-attr">&quot;unit&quot;</span>: <span class="hljs-string">&quot;Percent&quot;</span>,
      <span class="hljs-attr">&quot;aggregationTypes&quot;</span>: [
        <span class="hljs-string">&quot;auto&quot;</span>,
        <span class="hljs-string">&quot;avg&quot;</span>,
        <span class="hljs-string">&quot;max&quot;</span>,
        <span class="hljs-string">&quot;min&quot;</span>
      ]
    },
    {
      <span class="hljs-attr">&quot;metricId&quot;</span>: <span class="hljs-string">&quot;builtin:host.cpu.load&quot;</span>,
      <span class="hljs-attr">&quot;unit&quot;</span>: <span class="hljs-string">&quot;Ratio&quot;</span>,
      <span class="hljs-attr">&quot;aggregationTypes&quot;</span>: [
        <span class="hljs-string">&quot;auto&quot;</span>,
        <span class="hljs-string">&quot;avg&quot;</span>,
        <span class="hljs-string">&quot;max&quot;</span>,
        <span class="hljs-string">&quot;min&quot;</span>
      ]
    },
    {
      <span class="hljs-attr">&quot;metricId&quot;</span>: <span class="hljs-string">&quot;builtin:service.errors.server.count&quot;</span>,
      <span class="hljs-attr">&quot;unit&quot;</span>: <span class="hljs-string">&quot;Count&quot;</span>,
      <span class="hljs-attr">&quot;aggregationTypes&quot;</span>: [
        <span class="hljs-string">&quot;auto&quot;</span>,
        <span class="hljs-string">&quot;value&quot;</span>
      ]
    },
    {
      <span class="hljs-attr">&quot;metricId&quot;</span>: <span class="hljs-string">&quot;builtin:service.keyRequest.count.client&quot;</span>,
      <span class="hljs-attr">&quot;unit&quot;</span>: <span class="hljs-string">&quot;Count&quot;</span>,
      <span class="hljs-attr">&quot;aggregationTypes&quot;</span>: [
        <span class="hljs-string">&quot;auto&quot;</span>,
        <span class="hljs-string">&quot;value&quot;</span>
      ]
    }
  ]
}
</code></pre>
<p>The CSV table with header row looks like this. To obtain it, change the <strong>Accept</strong> header to <code>text/csv; header=present</code>.</p>
<pre><code class="language-http hljs">metricId,unit,aggregationTypes
builtin:host.cpu.idle,Percent,&quot;[auto, avg, max, min]&quot;
builtin:host.cpu.load,Ratio,&quot;[auto, avg, max, min]&quot;
builtin:service.errors.server.count,Count,&quot;[auto, value]&quot;
builtin:service.keyRequest.count.client,Count,&quot;[auto, value]&quot;
</code></pre>
<h4 id="response-code">Response code</h4>
<p>200</p>

  </div>
  <nav role="navigation" class="content--aside--top">
    <div class="toc-element">
      <h3 id="in-this-topic">In this topic</h3>
      <ul id="inline-toc" class="toc-list">
        <li class="toc-item"><a href="#parameters">Parameters
            
            </a></li>
        <li class="toc-item"><a href="#response-format">Response format
            
            </a></li>
        <li class="toc-item"><a href="#example">Example
            
            </a></li>
      </ul>
    </div>
      <div class="toc-element is-hidden-sm">
        <h3 id="related-topics">Related topics</h3>
        <ul class="toc-list">
            <li class="toc-item">
<a href="/support/help/dynatrace-api/basics/dynatrace-api-authentication/">Dynatrace API - Authentication</a>
</li>
<li class="toc-item">
<a href="/support/help/dynatrace-api/basics/dynatrace-api-response-codes/">Dynatrace API - Response codes</a>
</li>
<li class="toc-item">
<a href="/support/help/dynatrace-api/basics/access-limit/">Dynatrace API - Access limit</a>
</li>
<li class="toc-item">
<a href="/support/help/dynatrace-api/basics/preview-early-access/">Preview and Early Adopter releases for Dynatrace API</a>
</li>

        </ul>
      </div>
    <div class="toc-element">
      <h3 id="get-topic-updates">Get topic updates</h3>
        <p>Last modified on 2020-06-26 at 11:21 UTC</p>
      <div class="btngroup">
        <a target="_blank" rel="nofollow" href="/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/feed.xml" class="btn btn--primary">
          <svg role="img" class="icon icon--small icon--white" viewbox="0 0 512 512">
            <circle cx="129.4" cy="382.5" r="63.2"/>
            <path d="M109.1,179.7c-14.7,0-29.1,1.4-43.1,4.2v61c13.7-3.7,28.2-5.7,43.1-5.7c90.4,0,163.7,73.3,163.7,163.7
              c0,14.9-2,29.4-5.8,43.2h61.1c2.7-14,4.2-28.4,4.2-43.2C332.3,279.6,232.4,179.7,109.1,179.7z M119.3,66c-18.1,0-35.9,1.5-53.3,4.4v60.4c17.2-3.5,35-5.3,53.3-5.3c147.6,0,267.3,119.7,267.3,267.3
              c0,18.3-1.9,36.1-5.4,53.3h60.5c2.9-17.4,4.4-35.2,4.4-53.3C446,212.2,299.7,66,119.3,66z"/>
           </svg>
          RSS feed
        </a>
      </div>
    </div>
  </nav>
  </div>


      </article>
    </div>

    <footer class="footer">
      <div class="footer__legal">
        <ul class="footer__linklist footer__linklist--horizontal">
          <li class="footer__linkitem">
            <a href="https://www.dynatrace.com/company/trust-center/">Trust Center</a>
          </li>
          <li class="footer__linkitem">
            <a href="https://dynatrace.status.io/">Dynatrace status</a>
          </li>
          <li class="footer__linkitem">
            <a href="https://www.dynatrace.com/company/trust-center/policies/">Policies</a>
          </li>
          <li class="footer__linkitem">
            <a href="https://www.dynatrace.com/company/trust-center/terms-of-use/">Terms of use</a>
          </li>
          <li class="footer__linkitem">
            <a href="mailto:docfeedback@dynatrace.com?subject=Dynatrace%20Doc%20Feedback%20-%20%20-%20">Contact</a>
          </li>
          <li class="footer__linkitem">
            <a href="https://www.dynatrace.com/company/patents/">Patents</a>
          </li>
        </ul>
      </div>
    
      <div class="footer__socials theme--dark">
        <a href="https://www.facebook.com/Dynatrace/" class="footer__sociallink">
          <svg viewbox="0 1 23 23">
            <title>Facebook</title>
            <path d="M9.6,20.1v-7.3H7.2V9.6h2.4V8.4c0-2.2,1.6-4.1,3.6-4.1h2.6v3.2h-2.6c-0.3,0-0.6,0.3-0.6,0.9v1.3 h3.2v3.2h-3.2v7.3H9.6z"/>
          </svg>
        </a>
        <a href="https://twitter.com/Dynatrace" class="footer__sociallink">
          <svg viewbox="0 0 23 23">
            <title>Twitter</title>
            <path id="twitter" d="M14.4,5.6c1.3,0,2,0.4,2.6,1c0.6,0,1.3-0.4,1.7-0.6c0.1-0.1,0.3-0.2,0.4-0.2 C19,6.5,18.6,7,18.1,7.4c-0.1,0.1-0.2,0.2-0.4,0.3v0c0.7,0,1.3-0.3,1.9-0.5v0c-0.3,0.5-0.7,1-1.1,1.3c-0.2,0.1-0.3,0.3-0.5,0.4 c0,0.8,0,1.5-0.2,2.1c-0.8,3.8-3,6.3-6.5,7.4C10,18.8,8,19,6.6,18.6c-0.7-0.2-1.4-0.4-2-0.6c-0.3-0.1-0.6-0.3-0.9-0.5 c-0.1-0.1-0.2-0.1-0.3-0.2c0.3,0,0.7,0.1,1.1,0c0.3-0.1,0.7,0,1-0.1c0.8-0.2,1.4-0.4,2-0.7c0.3-0.2,0.7-0.4,0.9-0.6 c-0.4,0-0.7-0.1-1-0.2c-1.1-0.4-1.7-1.1-2.1-2.1c0.3,0,1.3,0.1,1.5-0.1c-0.4,0-0.8-0.3-1.1-0.4C4.7,12.6,4,11.7,4,10.2 c0.1,0.1,0.2,0.1,0.3,0.2c0.2,0.1,0.4,0.1,0.7,0.2c0.1,0,0.3,0.1,0.5,0c0,0,0,0,0,0c-0.2-0.2-0.4-0.3-0.6-0.5 c-0.6-0.7-1.1-1.8-0.7-3c0.1-0.3,0.2-0.6,0.4-0.9c0,0,0,0,0,0c0.1,0.1,0.2,0.2,0.3,0.3c0.3,0.4,0.6,0.7,1,1c1.2,1,2.3,1.5,4.1,2 c0.4,0.1,1,0.2,1.5,0.2c-0.2-0.4-0.1-1.1,0-1.6c0.3-1.1,0.9-1.8,1.9-2.2c0.2-0.1,0.5-0.2,0.7-0.2C14.2,5.6,14.3,5.6,14.4,5.6z"/>
          </svg>
        </a>
        <a href="https://www.instagram.com/dynatrace/" class="footer__sociallink">
          <svg viewbox="0 0 23 23">
            <title>Instagram</title>
            <path d="M11.5 5.35135124c2.0025898 0 2.2397887.0076375 3.0306375.04371915.7312383.03336718 1.1283672.15554024 1.3926492.25824806.3500746.13604922.5999184.29858985.8623563.56102698.2624488.26244845.4249894.5122926.5610382.8623684.1027071.26428048.2248813.66141058.2582481 1.39263757.0360812.7908602.0437187 1.02805982.0437187 3.030649 0 2.0025892-.0076378 2.2397884-.0437187 3.0306369-.0333668.7312383-.1555406 1.1283672-.2582481 1.3926493-.1360488.3500746-.2985894.5999183-.5610273.8623563-.2624488.2624488-.5122926.4249894-.8623672.5610383-.264282.102707-.6614113.2248812-1.3926492.258248-.7907344.0360813-1.0279117.0437188-3.0306375.0437188-2.00272578 0-2.23990273-.0076379-3.03063867-.0437188-.7312375-.0333668-1.12836797-.1555406-1.39264805-.258248-.35007578-.1360489-.59991953-.2985895-.86235625-.5610274-.26244414-.262443-.42498945-.5122926-.56103867-.8623672-.1027082-.2642821-.22488086-.6614114-.25824805-1.3926388-.03608086-.7908594-.04371836-1.0280586-.04371836-3.0306478 0-2.00258917.0076375-2.23978879.04371914-3.03063883.03336719-.73123754.15554024-1.12836803.25824805-1.39264812.13604922-.3500758.29858984-.59991995.56102695-.86235668.26244844-.26244885.51229219-.42498948.86236797-.56103871.26428047-.1027082.66141055-.22488087 1.3926375-.25824806C9.26021133 5.35898913 9.49741094 5.35135124 11.5 5.35135124zM11.5 4c-2.03688086 0-2.29228672.00862656-3.09223828.04512422-.79830234.03642696-1.34348086.16321095-1.82055664.34861643-.4931836.19166485-.91144844.44810822-1.32840547.86505942-.41695078.41695705-.67339414.83522191-.86505938 1.32840553-.18540546.47707542-.31218945 1.02225435-.3486164 1.82055674C4.00862695 9.20771355 4 9.46311357 4 11.5000004c0 2.036881.00862695 2.2922857.04512422 3.0922373.03642695.7983027.16321094 1.3434805.34861641 1.8205559.19166484.4931797.4481082.9114505.86505937 1.3284063.41695703.4169524.83522188.6733954 1.32840508.8650591.47707539.1854062 1.0222543.3121902 1.82055664.3486168C9.20771328 18.9913789 9.46311914 19 11.5 19c2.0368809 0 2.2922863-.0086211 3.0922379-.0451242.7983027-.036427 1.3434805-.1632106 1.8205558-.3486168.4931844-.1916637.9114504-.4481067 1.3284063-.8650591.4169523-.4169558.6733953-.8352219.865059-1.3284063.1854062-.4770754.3121902-1.0222532.3486168-1.8205559C18.9913727 13.7922861 19 13.5368814 19 11.5000004c0-2.03688097-.0086273-2.29228685-.0451242-3.09223845-.036427-.79830239-.1632106-1.34348093-.3486168-1.82055674-.1916637-.49318401-.4481067-.91144887-.865059-1.32840593-.4169559-.4169508-.8352219-.67339417-1.3284063-.86505942-.4770753-.18540547-1.0222531-.31218947-1.8205558-.34861642C13.7922863 4.00862656 13.5368816 4 11.5 4zm4.0250004 4.41718851c.4970565 0 .9000004-.40294392.9000004-.90000044 0-.49705651-.4029439-.90000043-.9000004-.90000043S14.625 7.02013156 14.625 7.51718807c0 .49705652.4029439.90000044.9000004.90000044zm-4.0017742-.74531332c-2.12704261 0-3.8513512 1.72430751-3.8513512 3.85135141 0 2.1270438 1.72430859 3.851349 3.8513512 3.851349 2.1270425 0 3.8513515-1.7243075 3.8513515-3.851349 0-2.12704155-1.7243097-3.85135141-3.8513515-3.85135141zm0 6.35134991c-1.3807114 0-2.50000003-1.1192883-2.50000003-2.4999981 0-1.3807126 1.11928863-2.50000018 2.50000003-2.50000018 1.3807129 0 2.5 1.11928758 2.5 2.50000018 0 1.3807098-1.1192871 2.4999981-2.5 2.4999981z">
          </path></svg>
        </a>
        <a href="https://www.linkedin.com/company/dynatrace" class="footer__sociallink">
          <svg viewbox="0 2 23 23">
            <title>LinkedIn</title>
            <path d="M7.5,19.1V9.8H4.4v9.4H7.5z M6,8.5c1.1,0,1.8-0.7,1.8-1.6 C7.7,6,7.1,5.3,6,5.3C4.9,5.3,4.2,6,4.2,6.9C4.2,7.8,4.9,8.5,6,8.5L6,8.5L6,8.5z"/>
            <path d="M9.3,19.1h3.1v-5.2c0-0.3,0-0.6,0.1-0.8 c0.2-0.6,0.7-1.1,1.6-1.1c1.1,0,1.6,0.9,1.6,2.1v5h3.1v-5.4c0-2.9-1.5-4.2-3.6-4.2c-1.7,0-2.4,0.9-2.8,1.6h0V9.8H9.3 C9.3,10.7,9.3,19.1,9.3,19.1L9.3,19.1z"/>
          </svg>
        </a>
        <a href="https://www.youtube.com/c/dynatrace" class="footer__sociallink">
          <svg viewbox="0 0 23 23">
            <title>Youtube</title>
            <path d="M16 11.503c0-.29-.117-.5-.352-.633l-6-3.752c-.242-.156-.495-.164-.76-.023-.26.14-.388.36-.388.656v7.504c0 .297.13.516.387.657.125.063.246.095.363.095.156 0 .29-.04.398-.118l6-3.75c.235-.134.352-.345.352-.634zm6 0c0 .75-.004 1.336-.012 1.758-.008.423-.04.957-.1 1.602-.058.644-.146 1.22-.263 1.73-.125.57-.395 1.05-.81 1.44-.412.39-.897.62-1.452.68-1.734.196-4.356.294-7.863.294-3.507 0-6.13-.098-7.863-.293-.555-.062-1.04-.29-1.46-.68-.418-.39-.688-.87-.814-1.442-.11-.507-.193-1.084-.252-1.728-.057-.645-.09-1.18-.098-1.6C1.004 12.838 1 12.25 1 11.5s.004-1.336.012-1.758c.008-.422.04-.955.1-1.6.058-.645.146-1.22.263-1.73.125-.57.395-1.05.81-1.44.412-.39.897-.62 1.452-.68C5.37 4.096 7.993 4 11.5 4c3.507 0 6.13.097 7.863.293.555.062 1.04.29 1.46.68.418.39.688.87.814 1.442.11.508.193 1.084.252 1.73.057.644.09 1.177.098 1.6.008.42.012 1.008.012 1.758z">
          </path></svg>
        </a>
        <a href="https://www.glassdoor.com/Overview/Working-at-Dynatrace-EI_IE309684.11,20.htm" class="footer__sociallink">
          <svg viewbox="0 0 509.3 506.3">
            <title>Glassdoor</title>
            <path d="M321.5,98.4c24.4,0,44.2,19.8,44.2,44.2v0H189V324c0,0.9-0.7,1.6-1.6,1.6h-41
              c-0.9,0-1.6-0.7-1.6-1.6V142.6v0c0-24.4,19.8-44.2,44.2-44.2h0H321.5z M321.5,363.4H144.9v0c0,24.4,19.8,44.2,44.2,44.2h132.5h0
              c24.4,0,44.2-19.8,44.2-44.2v0V182c0-0.9-0.7-1.6-1.6-1.6h-41c-0.9,0-1.6,0.7-1.6,1.6V363.4z">
          </path></svg>
        </a>
      </div>
    
      <p style="margin-top: 3rem; text-align: center;">&#xA9; 2020  Dynatrace LLC. All rights reserved</p>
    </footer>
    <script src="/support/doc/common/js/main-b4f4f2e730.js"></script>
    <script type="text/javascript">
      var dynatraceFont = dynatraceFont || {};
    
      dynatraceFont.cache = (function(s, xhr) {
    
        var cssPath = '/support/doc/common/css/fonts-a82fb11e97.css';
    
        if (s.getItem(dynatraceFont.storeKeyOld)) {
          s.removeItem(dynatraceFont.storeKeyOld);
        }
    
        if (s.getItem(dynatraceFont.storeKey) === null) {
          s.clear();
          var http = new xhr();
          http.open('GET', '//' + location.host + cssPath);
          http.onload = function() {
            dynatraceFont.addStyles(this.responseText);
            s.setItem(dynatraceFont.storeKey, this.responseText);
          }
          http.send();
        } else {
          dynatraceFont.addStyles(s.getItem(dynatraceFont.storeKey));
        }
    
      })(window.localStorage, XMLHttpRequest);
    </script>
    <script>
    loadCSS.loadCSS('/support/doc/common/css/photoswipe-224ad7d424.css');
    </script>
    
    <style>
    #us_report_button.rotate-right {
      bottom: 15%;
    }
    </style>
    <script type="text/javascript">
    var _usersnapconfig = {
      btnText: "Feedback", //button text
      langOverride: { i_feedback: 'Submit page feedback' }, //header text of widget dialog
      titleValue: document.title, //populates email subject with page title
      hideTour: true,
      customCssString: '.us-feedbackform .us-feedbackform-header,'
        + '.us-widget .us-widget-panel .us-widget-panel-header { background:#00a1b2 }'
        + '.us-btn { background:#00a1b2;border:none }'
        + '.us-btn:hover { background:#00848e;border:none }'
        + '.us-powered { visibility:hidden }'
        + '.us-widget .us-widget-panel .us-widget-panel-tool-base.active .us-widget-panel-toolbutton { background:#00a1b2 }'
        + '.us-widget .us-widget-panel .us-widget-panel-tool-base .us-widgetpanel-tool-button:hover, .us-widget'
        + '.us-widget-panel .us-widget-panel-tool-base .us-widgetpanel-tool-button.hover { background:#00a1b2 }'
        + '.us-widget .us-widget-panel { display: none; }',
    };
    (function() {
      var s = document.createElement("script");
      s.type = "text/javascript";
      s.async = true;
      s.src = '//api.usersnap.com/load/'+
              '8c65ac13-a16b-4968-a644-5ba1fc85abf5.js';
      var x = document.getElementsByTagName('script')[0];
      x.parentNode.insertBefore(s, x);
    })();
    </script>
    
    <script>
      // Google Analytics
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
      ga('create', 'UA-54510554-1', 'auto', 'dT', {'allowLinker': true});
      ga('dT.require', 'linker');
      ga('dT.linker:autoLink', ['dynatrace.com', 'compuwareapm.com', 'ruxit.com', 'dynatrace.de', 'dynatrace.es', 'dynatrace.fr', 'dynatrace.it']);
      ga('dT.send', 'pageview');
    </script>
    
  </body>
</html>
"""
soup = BeautifulSoup(text, "html.parser")
label = soup.find("h4", text="Authentication")
print(label.next_sibling.next_sibling)
