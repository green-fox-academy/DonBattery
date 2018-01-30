class ToolBox {

  isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
  }
  
  formatDate() {
    
    let date = new Date();
  
    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();
    let hour = date.getHours();
    let min = date.getMinutes();
    let sec = date.getSeconds();
  
    return `${year}.${month}.${day} ${hour}:${min}:${sec}`;
  }
  
  getIPaddress(inputString) {
    if (typeof inputString != "string") {
      return -1;
    } else {
      let temp = "";
      let i = 0;
      let foundStart = false;
      while (i < inputString.length) {
        if (this.isNumeric(inputString[i]) || foundStart) {
          foundStart = true;
          temp += inputString[i]
        };
        i++;
      };
      if (temp === "1" || temp === "127.0.0.1") {
        return "localhost"
      } else {
        return temp;
      };
    };
  }
  
};

module.exports = new ToolBox();