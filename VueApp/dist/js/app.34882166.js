(function(e){function t(t){for(var r,o,s=t[0],u=t[1],c=t[2],l=0,p=[];l<s.length;l++)o=s[l],Object.prototype.hasOwnProperty.call(a,o)&&a[o]&&p.push(a[o][0]),a[o]=0;for(r in u)Object.prototype.hasOwnProperty.call(u,r)&&(e[r]=u[r]);f&&f(t);while(p.length)p.shift()();return i.push.apply(i,c||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],r=!0,o=1;o<n.length;o++){var s=n[o];0!==a[s]&&(r=!1)}r&&(i.splice(t--,1),e=u(u.s=n[0]))}return e}var r={},o={app:0},a={app:0},i=[];function s(e){return u.p+"js/"+({about:"about"}[e]||e)+"."+{about:"2b2f6710"}[e]+".js"}function u(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,u),n.l=!0,n.exports}u.e=function(e){var t=[],n={about:1};o[e]?t.push(o[e]):0!==o[e]&&n[e]&&t.push(o[e]=new Promise((function(t,n){for(var r="css/"+({about:"about"}[e]||e)+"."+{about:"448cd8d8"}[e]+".css",a=u.p+r,i=document.getElementsByTagName("link"),s=0;s<i.length;s++){var c=i[s],l=c.getAttribute("data-href")||c.getAttribute("href");if("stylesheet"===c.rel&&(l===r||l===a))return t()}var p=document.getElementsByTagName("style");for(s=0;s<p.length;s++){c=p[s],l=c.getAttribute("data-href");if(l===r||l===a)return t()}var f=document.createElement("link");f.rel="stylesheet",f.type="text/css",f.onload=t,f.onerror=function(t){var r=t&&t.target&&t.target.src||a,i=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");i.code="CSS_CHUNK_LOAD_FAILED",i.request=r,delete o[e],f.parentNode.removeChild(f),n(i)},f.href=a;var d=document.getElementsByTagName("head")[0];d.appendChild(f)})).then((function(){o[e]=0})));var r=a[e];if(0!==r)if(r)t.push(r[2]);else{var i=new Promise((function(t,n){r=a[e]=[t,n]}));t.push(r[2]=i);var c,l=document.createElement("script");l.charset="utf-8",l.timeout=120,u.nc&&l.setAttribute("nonce",u.nc),l.src=s(e);var p=new Error;c=function(t){l.onerror=l.onload=null,clearTimeout(f);var n=a[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;p.message="Loading chunk "+e+" failed.\n("+r+": "+o+")",p.name="ChunkLoadError",p.type=r,p.request=o,n[1](p)}a[e]=void 0}};var f=setTimeout((function(){c({type:"timeout",target:l})}),12e4);l.onerror=l.onload=c,document.head.appendChild(l)}return Promise.all(t)},u.m=e,u.c=r,u.d=function(e,t,n){u.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},u.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,t){if(1&t&&(e=u(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(u.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)u.d(n,r,function(t){return e[t]}.bind(null,r));return n},u.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return u.d(t,"a",t),t},u.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},u.p="/",u.oe=function(e){throw console.error(e),e};var c=window["webpackJsonp"]=window["webpackJsonp"]||[],l=c.push.bind(c);c.push=t,c=c.slice();for(var p=0;p<c.length;p++)t(c[p]);var f=l;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),o=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("v-app-bar",{attrs:{app:""}},[n("v-img",{attrs:{src:"https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1200px-Utoronto_coa.svg.png","aspect-ratio":"1","max-width":"50","max-height":"50"}}),n("v-toolbar-title",{staticClass:"headline"},[n("span",[e._v("UTSC")]),n("span",{staticClass:"font-weight-light"},[e._v(" Course Tree")])]),n("v-toolbar-items",[n("navbar")],1),n("v-spacer"),n("v-toolbar-items",[n("v-btn",{attrs:{text:""}},[e._v("Login")])],1)],1),n("v-content",[n("router-view")],1)],1)},a=[],i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("nav",[n("ul",[n("li",[n("router-link",{attrs:{exact:"",to:"/"}},[e._v("Home")])],1),n("li",[n("router-link",{attrs:{exact:"",to:"/courses"}},[e._v("Courses")])],1),n("li",[n("router-link",{attrs:{exact:"",to:"/treeview"}},[e._v("TreeView")])],1),n("li",[n("router-link",{attrs:{exact:"",to:"/information"}},[e._v("Information")])],1)])])},s=[],u={name:"NavBar"},c=u,l=(n("c7c0"),n("2877")),p=Object(l["a"])(c,i,s,!1,null,"7a379048",null),f=p.exports,d={name:"App",components:{navbar:f},data:function(){return{}}},v=d,m=n("6544"),h=n.n(m),b=n("7496"),g=n("40dc"),y=n("8336"),w=n("a75b"),_=n("adda"),x=n("2fa4"),C=n("2a7f"),j=Object(l["a"])(v,o,a,!1,null,null,null),k=j.exports;h()(j,{VApp:b["a"],VAppBar:g["a"],VBtn:y["a"],VContent:w["a"],VImg:_["a"],VSpacer:x["a"],VToolbarItems:C["a"],VToolbarTitle:C["b"]});n("d3b7");var O=n("8c4f"),T=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"home"},[n("HomePage",{attrs:{msg:"Welcome to Your Vue.js App"}})],1)},E=[],S=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-container",{staticClass:"home-container"},[n("v-col",{staticClass:"col-container"},[n("v-row",[n("h1",{staticClass:"heading1"},[e._v(" A new way "),n("br"),e._v(" to view UTSC courses "),n("br"),e._v(" without all the tabs! ")])]),n("v-row",{staticClass:"spacer"}),n("v-row",[n("h1",{staticClass:"heading2"},[e._v(" Designed by students, for students. ")])])],1)],1)},V=[],A={components:{},data:function(){return{whatsNext:[{text:"Explore components",href:"https://vuetifyjs.com/components/api-explorer"},{text:"Select a layout",href:"https://vuetifyjs.com/layout/pre-defined"},{text:"Frequently Asked Questions",href:"https://vuetifyjs.com/getting-started/frequently-asked-questions"}]}}},P=A,N=(n("cf38"),n("62ad")),B=n("a523"),L=n("0fd9"),q=Object(l["a"])(P,S,V,!1,null,"c52d3b6a",null),U=q.exports;h()(q,{VCol:N["a"],VContainer:B["a"],VRow:L["a"]});var $={name:"home",components:{HomePage:U}},H=$,I=Object(l["a"])(H,T,E,!1,null,null,null),M=I.exports;r["a"].use(O["a"]);var D=[{path:"/",name:"home",component:M},{path:"/courses",name:"courses",component:function(){return n.e("about").then(n.bind(null,"1a2f"))}},{path:"/treeview",name:"treeview",component:function(){return n.e("about").then(n.bind(null,"a232"))}},{path:"/information",name:"information",component:function(){return n.e("about").then(n.bind(null,"5798"))}}],F=new O["a"]({mode:"history",base:"/",routes:D}),J=F,K=n("f309");r["a"].use(K["a"]);var Q=new K["a"]({icons:{iconfont:"mdi"}}),R=(n("41e9"),n("ecee")),W=n("c074"),Y=n("ad3d");R["c"].add(W["a"]),r["a"].component("font-awesome-icon",Y["a"]),r["a"].config.productionTip=!1,new r["a"]({router:J,vuetify:Q,render:function(e){return e(k)}}).$mount("#app")},c7c0:function(e,t,n){"use strict";var r=n("d3e7"),o=n.n(r);o.a},ce59:function(e,t,n){},cf38:function(e,t,n){"use strict";var r=n("ce59"),o=n.n(r);o.a},d3e7:function(e,t,n){}});
//# sourceMappingURL=app.34882166.js.map