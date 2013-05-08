function showContact(event)
{
    $('.verticalFloater').animate({
        'margin-bottom': $('#contact').height() * -1 / 1.8 + 'px'
    }, 500);
    $('#home').slideUp(500);
    $('#contact').slideDown(500);
}

function showHome(event)
{
    $('.verticalFloater').animate({
        'margin-bottom': '-160px'
    }, 500);
    $('#home').slideDown(500);
    $('#contact').slideUp(500);
}

function updateConsole()
{
    var actualTop = parseInt($('#console').css('top'));
    var lineHeight = parseInt($('#console').css('line-height'));
    var consoleHeight = $('#console').height();
    var newHeight = actualTop - lineHeight;

    if(newHeight <= consoleHeight * -1)
        $('#console').css({ 'top': '92px' });
    else
        $('#console').css({ 'top': newHeight + 'px' });

}

function openLink(event)
{
    var itemClass = $(this).children('.link').attr('class').replace('link ', '');
    var targetUrl = '';
    
    switch(itemClass)
    {
        case 'github':
            targetUrl = 'https://github.com/fernando-jascovich';
        break;
        case 'twitter':
            targetUrl = 'https://twitter.com/fernando_ej';
        break;
        case 'linkedin':
            targetUrl = 'http://www.linkedin.com/pub/fernando-jascovich/29/ab9/87b';
        break;
        case 'mail':
            targetUrl = 'mailto:fernando.ej@gmail.com';
        break;
        case 'skype':
            targetUrl = 'skype:fernando.jascovich?chat';
        break;
        case 'icq':
            targetUrl = 'http://www.icq.com/people/662318579/edit/en';
        break;
    }

    window.open(targetUrl, '_blank');
}

function toggleLinks(event)
{
    if($(this).siblings('.linksItself').css('display') == 'none')
        $(this).siblings('.linksItself').slideDown(500);
    else
        $(this).siblings('.linksItself').slideUp(500);
}

function bindHandlers(event)
{
    $('#contactLink').on('click', showContact);
    $('#homeLink').on('click', showHome);
    setInterval('updateConsole();', 1500);
    $('.item').on('click', openLink);
    $('#links').on('click', toggleLinks);
}

$(document).on('ready', bindHandlers);