/*
 *             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 *                    Version 2, December 2004
 *
 * Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 * Everyone is permitted to copy and distribute verbatim or modified
 * copies of this license document, and changing it is allowed as long
 * as the name is changed.

 *           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 *  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
 *
 * 0. You just DO WHAT THE FUCK YOU WANT TO.
 * Author: Bogomil "Bogo" Shopov <shopov.bogomil@gmail.com>
 * 
 * 
 * Thanks goes to: Mike Kaply && Wladimir Palant for their help and code
 * 
 * */



/*
 * include components and functions we need to create a new protocol
* */

const Ci = Components.interfaces;
const Cc = Components.classes;
const Cr = Components.results;
const nsIProtocolHandler = Ci.nsIProtocolHandler;
Components.utils.import("resource://gre/modules/XPCOMUtils.jsm");

/*
 * function to handle requests.
 * # TODO: Websocket to Python to get things
 * */
function  WhereToGo(key){
    return "http://localhost:8000";
}

function AboutScott() {
}

AboutScott.prototype = {
  scheme: "scott",
  protocolFlags: nsIProtocolHandler.URI_NORELATIVE |
                 nsIProtocolHandler.URI_NOAUTH |
                 nsIProtocolHandler.URI_LOADABLE_BY_ANYONE,

  newURI: function(aSpec, aOriginCharset, aBaseURI)
  {
    var uri = Cc["@mozilla.org/network/simple-uri;1"].createInstance(Ci.nsIURI);
    uri.spec = aSpec;
    return uri;
  },

  newChannel: function(aURI)
  {
    var ioservice = Cc["@mozilla.org/network/io-service;1"].getService(Ci.nsIIOService);
    var hash = aURI.spec.split("://")[1];
    if (!hash) {
        hash = aURI.spec.split(":")[1];
    }
    var wheretogo = WhereToGo(hash);
    var uri = ioservice.newURI(wheretogo, null, null);
    var channel = ioservice.newChannelFromURI(uri, null).QueryInterface(Ci.nsIHttpChannel);
    return channel;
  },
  classDescription: "Scott Basic Protocol Handler",
  contractID: "@mozilla.org/network/protocol;1?name=" + "scott",
  classID: Components.ID('{b1dc9a3f-6f26-442d-a5e6-5d8600414625}'),
  QueryInterface: XPCOMUtils.generateQI([Ci.nsIProtocolHandler])
}

if (XPCOMUtils.generateNSGetFactory)
  var NSGetFactory = XPCOMUtils.generateNSGetFactory([AboutScott]);
else
  var NSGetModule = XPCOMUtils.generateNSGetModule([AboutScott]);
