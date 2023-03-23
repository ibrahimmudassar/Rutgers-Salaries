$.get("https://raw.githubusercontent.com/ibrahimmudassar/Rutgers-Salaries/main/README.md", function(data) {
  var converter = new showdown.Converter();

  document.getElementById('readme').innerHTML = converter.makeHtml(data);
});


$('#mainTable').DataTable({
  stateSave: true,
  order: [[4, 'desc']],

  scrollY: '98vh',
  scrollCollapse: true,

  lengthMenu: [
    [15, 50, 100, -1],
    [15, 50, 100, 'All'],
  ],

  deferRender: true,
  ajax: {
    url: "https://raw.githubusercontent.com/ibrahimmudassar/Rutgers-Salaries/main/rutgers_salaries.csv",
    dataType: "text",
    dataSrc: function (csvdata) {
    return $.csv.toObjects(csvdata);
  }},

  columns: [
    { data: "Name" },
    { data: "Campus" },
    { data: "Depart" },
    { data: "Title" },
    { data: "Total Pay", 
      render: function (data) {
        var number = $.fn.dataTable.render
          .number(',', '.', 2, '$')
          .display(data);

        return number;
    }, },
  ]
});