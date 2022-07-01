function datosDetalleCompras(){
  let data = [];
  var item = {};
  $('#detalleProducto tr').each(function() {
      if (!this.rowIndex) return; // skip first row
        column1 = this.cells[0].innerHTML;
        column2 = parseInt(this.cells[1].innerHTML.replace(/\D/g,''));
        column3 = this.cells[2].innerHTML;
        column4 = parseInt(this.cells[3].innerHTML.replace(/\D/g,''));
        column5 = parseInt(this.cells[4].innerHTML.replace(/\D/g,''));
        column6 = parseInt(this.cells[5].innerHTML.replace(/\D/g,''));
        column7 = parseInt(this.cells[6].innerHTML.replace(/\D/g,''));
        item = column1+","+ 
          column2+","+
          column3+","+
          column4+","+
          column5+","+
          column6+","+
          column7;
      data.push(item);
      });
    return data;
  }
