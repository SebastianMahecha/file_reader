from django.conf import settings
from django.shortcuts import render, redirect
from .helpers.pdf_reader_helper import PDFReaderHelper

def pdf_reader_view(request):
    
    pdf_reader_helper = PDFReaderHelper()   
    vista = 'pdf_reader'
    context = { 
        'vista': vista,
        'files': pdf_reader_helper.get_files(),
        'base_pool_pdf': settings.BASE_POOL_PDF,
        'base_pool_word': settings.BASE_POOL_WORD,
    }
    return render(request,  'main/'+vista+'.html', context)

def pdf_reader_new_view(request):
            
    vista = 'pdf_reader_new'
    context = { 
        'vista': vista,
    }
    return render(request,  'main/'+vista+'.html', context)

def pdf_reader_save(request):

    pdf = request.FILES["pdf"]    
    pdf_reader_helper = PDFReaderHelper()
    pdf_reader_helper.create_file(pdf)

    return redirect("/main/reader/pdf/view")
