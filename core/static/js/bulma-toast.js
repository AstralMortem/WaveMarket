/*!
 * bulma-toast 2.4.2 
 * (c) 2018-present @rfoel <rafaelfr@outlook.com> 
 * Released under the MIT License.
 */
(function(a,b){"object"==typeof exports&&"undefined"!=typeof module?b(exports):"function"==typeof define&&define.amd?define(["exports"],b):(a="undefined"==typeof globalThis?a||self:globalThis,b(a.bulmaToast={}))})(this,function(a){'use strict';function b(a,b){var c=Object.keys(a);if(Object.getOwnPropertySymbols){var d=Object.getOwnPropertySymbols(a);b&&(d=d.filter(function(b){return Object.getOwnPropertyDescriptor(a,b).enumerable})),c.push.apply(c,d)}return c}function c(a){for(var c,d=1;d<arguments.length;d++)c=null==arguments[d]?{}:arguments[d],d%2?b(Object(c),!0).forEach(function(b){g(a,b,c[b])}):Object.getOwnPropertyDescriptors?Object.defineProperties(a,Object.getOwnPropertyDescriptors(c)):b(Object(c)).forEach(function(b){Object.defineProperty(a,b,Object.getOwnPropertyDescriptor(c,b))});return a}function d(a,b){if(!(a instanceof b))throw new TypeError("Cannot call a class as a function")}function e(a,b){for(var c,d=0;d<b.length;d++)c=b[d],c.enumerable=c.enumerable||!1,c.configurable=!0,"value"in c&&(c.writable=!0),Object.defineProperty(a,c.key,c)}function f(a,b,c){return b&&e(a.prototype,b),c&&e(a,c),a}function g(a,b,c){return b in a?Object.defineProperty(a,b,{value:c,enumerable:!0,configurable:!0,writable:!0}):a[b]=c,a}function h(){var a;return null!==(a=o)&&void 0!==a?a:document}function i(a,b,c,d,e,f){if(n.position)return n.position;var g=h().createElement("div");return g.setAttribute("style","width:100%;z-index:99999;position:fixed;pointer-events:none;display:flex;flex-direction:column;padding:15px;"+p(b,c,d,e,f)),a.appendChild(g),n.position=g,g}function j(a){for(var b in n)n[b].remove();n={},o=a}function k(a){if(!a.message)throw new Error("message is required");var b=c(c({},m),a),d=new q(b),e=i(b.appendTo||h().body,b.position||m.position,b.offsetTop||m.offsetTop,b.offsetBottom||m.offsetBottom,b.offsetLeft||m.offsetLeft,b.offsetRight||m.offsetRight);if(b.single)for(var f=e.lastElementChild;f;)e.removeChild(f),f=e.lastElementChild;e.appendChild(d.element)}var l={duration:2e3,position:"top-right",closeOnClick:!0,opacity:1,single:!1,offsetTop:0,offsetBottom:0,offsetLeft:0,offsetRight:0,extraClasses:""},m=c({},l),n={},o=null,p=function(a,b,c,d,e){return"top-left"===a?"left:".concat(d,";top:").concat(b,";text-align:left;align-items:flex-start;"):"top-right"===a?"right:".concat(e,";top:").concat(b,";text-align:right;align-items:flex-end;"):"top-center"===a?"top:".concat(b,";left:0;right:0;text-align:center;align-items:center;"):"bottom-left"===a?"left:".concat(d,";bottom:").concat(c,";text-align:left;align-items:flex-start;"):"bottom-right"===a?"right:".concat(e,";bottom:").concat(c,";text-align:right;align-items:flex-end;"):"bottom-center"===a?"bottom:".concat(c,";left:0;right:0;text-align:center;align-items:center;"):"center"===a?"top:0;left:0;right:0;bottom:0;flex-flow:column;justify-content:center;align-items:center;":void 0},q=/*#__PURE__*/function(){function a(b){var c=this;d(this,a),this.element=h().createElement("div"),this.opacity=b.opacity,this.type=b.type,this.animate=b.animate,this.dismissible=b.dismissible,this.closeOnClick=b.closeOnClick,this.message=b.message,this.duration=b.duration,this.pauseOnHover=b.pauseOnHover,this.offsetTop=b.offsetTop,this.offsetBottom=b.offsetBottom,this.offsetLeft=b.offsetLeft,this.offsetRight=b.offsetRight,this.extraClasses=b.extraClasses;var e="width:auto;pointer-events:auto;display:inline-flex;white-space:pre-wrap;opacity:".concat(this.opacity,";"),f=["notification",this.extraClasses];if(this.type&&f.push(this.type),this.animate&&this.animate["in"]){var g="animate__".concat(this.animate["in"]),i=this.animate.speed?"animate__".concat(this.animate.speed):"animate__faster";f.push("animate__animated ".concat(g," ").concat(i)),this.onAnimationEnd(function(){return c.element.classList.remove(g)})}if(this.element.className=f.join(" "),this.dismissible){var j=h().createElement("button");j.className="delete",j.addEventListener("click",function(){c.destroy()}),this.element.insertAdjacentElement("afterbegin",j)}else e+="padding: 1.25rem 1.5rem";this.closeOnClick&&this.element.addEventListener("click",function(){c.destroy()}),this.element.setAttribute("style",e),"string"==typeof this.message?this.element.insertAdjacentHTML("beforeend",this.message):this.element.appendChild(this.message);var k=new r(function(){c.destroy()},this.duration);this.pauseOnHover&&(this.element.addEventListener("mouseover",function(){k.pause()}),this.element.addEventListener("mouseout",function(){k.resume()}))}return f(a,[{key:"destroy",value:function(){var a=this;this.animate&&this.animate.out?(this.element.classList.add("animate__".concat(this.animate.out)),this.onAnimationEnd(function(){a.removeParent(a.element.parentNode),a.element.remove(),delete n.position})):(this.removeParent(this.element.parentNode),this.element.remove(),delete n.position)}},{key:"removeParent",value:function(a){a&&1>=a.children.length&&a.remove()}},{key:"onAnimationEnd",value:function(){var a=0<arguments.length&&void 0!==arguments[0]?arguments[0]:function(){},b={animation:"animationend",OAnimation:"oAnimationEnd",MozAnimation:"mozAnimationEnd",WebkitAnimation:"webkitAnimationEnd"};for(var c in b)if(void 0!==this.element.style[c]){this.element.addEventListener(b[c],function(){return a()});break}}}]),a}(),r=/*#__PURE__*/function(){function a(b,c){d(this,a),this.timer,this.start,this.remaining=c,this.callback=b,this.resume()}return f(a,[{key:"pause",value:function(){"undefined"==typeof document||(window.clearTimeout(this.timer),this.remaining-=new Date-this.start)}},{key:"resume",value:function(){"undefined"==typeof document||(this.start=new Date,window.clearTimeout(this.timer),this.timer=window.setTimeout(this.callback,this.remaining))}}]),a}();a.resetDefaults=function(){m=c({},l)},a.setDefaults=function(a){m=c(c({},l),a)},a.setDoc=j,a.toast=k,Object.defineProperty(a,"__esModule",{value:!0})});