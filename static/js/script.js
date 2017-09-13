/*function onReady(callback) {
    var intervalID = window.setInterval(checkReady, 1000);

    function checkReady() {
        if (document.getElementsByTagName('body')[0] !== undefined) {
            window.clearInterval(intervalID);
            callback.call(this);
        }
    }
}

function show(id, value) {
    document.getElementById(id).style.display = value ? 'block' : 'none';
}

onReady(function () {
    show('loading', false);
    show('container_page', true);
});*/


function main() {
    setTimeout(function() {
        document.getElementById('loading').className = 'not_loadded';
        document.getElementById('container_page').className = 'loaded';
        setTimeout(function() {
            document.getElementById('loading').className = 'finished';            
        }, 1000);
    }, 2000);
}

window.onload = main();


$(document).ready(function() {
    $('#fullpage').fullpage({
        'anchors': ['home', 'about_us', 'our_services', 'gallery', 'contact_us'],
        'menu': '#menu',
        'sectionsColor': ['#EDE9E3', '#EDE9E3', '#EDE9E3', '#EDE9E3', '#EDE9E3'],
        'navigation': true,
        'navigationPosition': 'right',
        'navigationTooltips': ['Home', 'About Us', 'Our Services', 'Gallery', 'Contact Us'],
        'scrollingSpeed': 850,
        'afterLoad' : function(anchorLink, index){
            if(index == 1){
                $('#section1 img').delay(2800).queue(function(next){
                    $('#section1 img').addClass('bounceInDown animated');
                    $('#section1 h2').addClass('bounceInUp animated');
                    next();
                });
            }
            /*else if(index == 2){
                $('#pers1, #pers2').addClass('active');
                $('.box').addClass('fadeInUp animated');
            }
            else if(index == 3){
                $('#starting img').addClass('active');
                $('#starting .text span').addClass('fadeInLeftBig animated');
            }
            else if(index == 4){
                $('#from h2').addClass('bounceIn animated');
            }
            else if(index == 5){
                $('#fotoslider h2').addClass('fadeInUp animated');
            }
            else if(index == 6){
                $('#ourproject .title').addClass('fadeInDown animated');
            }
            else if(index == 7){
                $('#sayhello .middle .title').addClass('fadeInDown animated');
            }*/
        }
    });
});