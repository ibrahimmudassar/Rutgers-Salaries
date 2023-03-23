$(document).ready(function () {
  // Setup - add a text input to each footer cell
  $('#mainTable tfoot th').each(function () {
      var title = $(this).text();
      $(this).html('<input type="text" placeholder="Search ' + title + '" />');
  });

  // DataTable
  var table = $('#mainTable').DataTable({
      initComplete: function () {
          // Apply the search
          this.api()
              .columns()
              .every(function () {
                  var that = this;

                  $('input', this.footer()).on('keyup change clear', function () {
                      if (that.search() !== this.value) {
                          that.search(this.value).draw();
                      }
                  });
              });
      },
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
});