// Author: Thomas Davis <thomasalwyndavis@gmail.com>
// Filename: main.js

// Require.js allows us to configure shortcut alias
// Their usage will become more apparent futher along in the tutorial.
require.config({
  shim: {
    'backbone': {
        deps: ['jquery', 'underscore'],
        exports: 'Backbone'
    },
    'underscore': {
      exports: '_'
    },
  },

  paths: {
    jquery: 'libs/jquery/jquery-min',
    underscore: 'libs/underscore/underscore-min',
    backbone: 'libs/backbone/backbone-min',
    backbone_localstorage: 'libs/backbone/backbone-localstorage',
    templates: '../templates'
  }

});

require([
  // Load our app module and pass it to our definition function
  'todos/appView',

], function(App){
  // The "app" dependency is passed in as "App"
  // Again, the other dependencies passed in are not "AMD" therefore don't pass a parameter to this function
  new App();
});
