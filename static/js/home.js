const editFile = row => {
  console.log(row)
}

$(function() {
    let table = $('#table').dataTable({
      ajax: '/file-list',
      ordering: false,
      searching: false,
      columns: [
        {
          data: 'key'
        }, {
          data: 'last_modified',
          width: '200px'
        }, {
          data: 'last_modified',
          width: '100px',
          render: (data, type, row) => {
            return `<a class="btn btn-success" href="/mtd/file-edit?key=${row.key}">Edit</button>`
          }
        }
      ]
    })
});