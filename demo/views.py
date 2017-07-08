from common.mymako import render_mako_context
def demo(request):
    return render_mako_context(request,'/demo/demo.html')
def demo1(request):
    return  render_mako_context(request,'/demo/demo1.html')