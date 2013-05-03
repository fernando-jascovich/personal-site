var topOffset = 55;

function adjustHeight(event)
{
    var fixedHeight = document.body.clientHeight - $('.actionBar').height() - $(event.data.targetSelector).offset().top - topOffset;

    $(event.data.targetSelector).css({
        'height': fixedHeight + 'px'
    });

    var newOffset = $('#backendForm #' + $('.simpleHeader > ul > li.active').attr('id')).offset().top;

    $('html, body').scrollTop(newOffset - topOffset);
}

function bindHandlers(event)
{
    $('html, body').scrollTop(0);
    $(window).on('resize', {'targetSelector': '#backendForm'}, adjustHeight);
    $('.simpleHeader > ul > li').on('click', scrollToElement);
    $('.actionBar #save').on('click', saveBackEndForm);
    initializeNavBar('#backendForm');
}

function saveBackEndForm(event)
{
    $('#backendForm').submit();
}

function initializeNavBar(targetSelector)
{
    $('.simpleHeader > ul > li').removeClass('active');

    var steps = $(targetSelector).children('div');
    var navItems = $('.simpleHeader > ul > li');
    var actualPos = 0;

    for(var i = 0; i < steps.length; i++)
    {
        if($(window).scrollTop() >= $(steps[i]).offset().top - topOffset)
            actualPos = i;
    }

    $(navItems[actualPos]).addClass('active');
}

function scrollToElement(event)
{
    $('html, body').animate({
        scrollTop: $('#backendForm #' + event.currentTarget.id).offset().top - topOffset + 'px'
    }, 500, function(){ 
        initializeNavBar('#backendForm');
    });
}

$(document).on('ready', bindHandlers);
$(document).on('ready', {'targetSelector': '#backendForm'}, adjustHeight);