$(document).ready(function () {
  // DataTable
  var table = $("#mainTable").DataTable({
    order: [[5, "desc"]],

    scrollY: "98vh",
    scrollCollapse: true,

    lengthMenu: [
      [15, 50, 100, -1],
      [15, 50, 100, "All"],
    ],

    searchBuilder: true,

    responsive: true,
    columnDefs: [
      { responsivePriority: 1, targets: 0 },
      { responsivePriority: 2, targets: -1 },
    ],

    deferRender: true,
    ajax: {
      url: "https://raw.githubusercontent.com/ibrahimmudassar/Rutgers-Salaries/main/rutgers_salaries.csv",
      dataType: "text",
      dataSrc: function (csvdata) {
        return $.csv.toObjects(csvdata);
      },
    },

    columns: [
      { data: "Name" },
      { data: "Campus" },
      { data: "Department" },
      { data: "Title" },
      { data: "Hire Date" },
      {
        data: "Gross Pay",
        render: function (data) {
          var number = $.fn.dataTable.render
            .number(",", ".", 0, "$")
            .display(data);

          return number;
        },
      },
    ],
  });
  table.searchBuilder.container().prependTo(table.table().container());
});
