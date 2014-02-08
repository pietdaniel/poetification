$(document).ready(function(){
  $('#entitylist').magicSuggest(
    {
      maxSelection: null,
      allowFreeEntries: 'false',
      selectionPosition: 'right',
      selectionStacked: 'true',
      id: 'entitylist',
      name: 'entitylist',
      data: '/entity_list/',
      emptyText: 'Select entities',
    }
  );
  $('#risklist').magicSuggest(
    {
      maxSelection: null,
      allowFreeEntries: 'false',
      selectionPosition: 'right',
      selectionStacked: 'true',
      id: 'risklist',
      name: 'risklist',
      data: '/risk_list/',

      emptyText: 'Select risks'
    }
  );
  $('#dates').daterangepicker(
    {
      ranges: {
        'Today': [moment(), moment()],
        'Yesterday': [moment().subtract('days', 1), moment().subtract('days', 1)],
        'Last 7 Days': [moment().subtract('days', 6), moment()],
        'Last 30 Days': [moment().subtract('days', 29), moment()],
        'This Month': [moment().startOf('month'), moment().endOf('month')],
        'Last Month': [moment().subtract('month', 1).startOf('month'), moment().subtract('month', 1).endOf('month')]
      },
      startDate: moment().subtract('days', 29),
      endDate: moment(),
      format: 'YYYY-MM-DD'
    },
    function(start, end) {
      $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
    })
  // $('#aggregation_type').combobox();
});
