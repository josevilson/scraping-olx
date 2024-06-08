
-- Script para fazer o scroll da pagina.

function main(splash, args)
        splash:set_viewport_size(1024, 768)
        splash:go(args.url)
        splash:wait(4)
  			splash:wait(3)
        
        local scroll_to = splash:jsfunc("window.scrollTo")
        scroll_to(0, 10000)  -- Scroll down
        splash:wait(3)
  			scroll_to(10000, 20000) 
        splash:wait(3)
  			scroll_to(20000, 30000)
        splash:wait(3)
        
        return {
            html = splash:html(),
            png = splash:png(),
            har = splash:har(),
        }
    end