define([
  'underscore',
  'backbone'
], function(_, Backbone){

  var Todo = Backbone.Model.extend({
    urlRoot: 'todos/',
    id: null,
    defaults: {
        id: null,
        title: "empty todo...",
        // order: this.collection.nextOrder(),
        done: false
    },
    // Toggle the `done` state of this todo item.
    toggle: function() {
      this.save({done: !this.get("done")});
    }

  });

  return Todo;
});