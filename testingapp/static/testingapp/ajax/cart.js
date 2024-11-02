


function _(c){ return document.getElementById(c);}
const _tkn = _('us_tkn').children[0].getAttribute('value');
 var _name = _('name'), discription = _('dex'), image = _('image').getAttribute("user_img"), btn = _('get_btn')
 console.log(image)

btn.addEventListener('click', () =>{
var _url = '/add_to_cart/';
var form_data = new FormData();
 form_data.append('name', _name.innerText);
 form_data.append('describ', discription.innerText);
 form_data.append('image', image);

 fetch(_url, {
    method: 'POST',
    headers: {
     'X-CSRFToken': _tkn,
    },
    body: form_data,
 })
 .then(response => response.json())
 .then(data => {
     console.log('success:', data);
     if (data.S) {
         console.log(data.S)
     }else if(data.W){
         console.log(data.W);
     }else if(data.E) {
         console.log(data.E)
     }else{
         console.log('sorry an error occured')
     }
 })
 .catch((error) => {
     console.error('Error:', error);
 })

})
