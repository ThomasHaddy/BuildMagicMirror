/* Magic Mirror Config
 *
 * By Michael Teeuw https://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information on how you can configure this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */
var config =
{
   // Address to listen on, can be:
	// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
	// - another specific IPv4/6 to listen on a specific interface
	// - "0.0.0.0", "::" to listen on any interface
	// Default, when address config is left out or empty, is "localhost"
   address: "localhost",
	port: 8080,
   // The URL path where MagicMirror is hosted. If you are using a Reverse proxy
	// you must set the sub path here. basePath must end with a /
	basePath: "/",
   // Set [] to allow all IP addresses
	// or add a specific IPv4 of 192.168.1.5 :
	// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
	// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
   // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"],
	useHttps: false, 		   // Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "", 	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "", 	// HTTPS Certificate path, only require when useHttps is true
	language: "en",
	logLevel: ["INFO", "LOG", "WARN", "ERROR"], // Add "DEBUG" for even more logging
	timeFormat: 24,
	units: "metric",
	// serverOnly:  true/false/"local" ,
	// local for armv6l processors, default
	//   starts serveronly and then starts chrome browser
	// false, default for all NON-armv6l devices
	// true, force serveronly mode, because you want to.. no UI on this device

	modules:
   [
		{
			module:     "updatenotification",
			position:   "top_bar"
		},
		{
			module:     "clock",
			position:   "top_bar",
         config:
         {
		      lat:              0,
		      lon:              0,
            displaySeconds:   true,
            showPeriodUpper:  true,
            showDate:         true,
            showSunTimes:     true,
            timeFormat:       12,
         }
		},
		{
			module:     "newsfeed",
			position:   "bottom_bar",
			config:
         {
				feeds:
            [
					{
						title:   "New York Times",
						url:     "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
					}
				],
				showSourceTitle:        true,
				showPublishDate:        true,
				broadcastNewsFeeds:     true,
				broadcastNewsUpdates:   true
			}
		},
		{
  			module:     "MMM-NowPlayingOnSpotify",
  			position:   "top_right",
  			config:
         {
    		   clientID:      "",
    			clientSecret:  "",
    			accessToken:   "",
    			refreshToken:  ""
  			}
		},
      {
         module:     "MMM-3Day-Forecast",
         position:   "top_left",
	      config:
         {
		      api_key:    "",
		      lat:        0,
		      lon:        0,
		      units:      "I",
		      lang:       "en",
		      interval:   900000
	      }
      },
	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
