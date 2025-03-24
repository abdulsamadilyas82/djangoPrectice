from django.http import HttpResponse, JsonResponse
from bookApp.models import Books
from bookApp.serializers import BookSerializer


def viewBooks(request):
    books = Books.objects.all()
    serializer = BookSerializer(books, many=True)

    #
    # book_details = """
    # <html>
    # <head>
    #     <title>Books List</title>
    #     <style>
    #         table { width: 60%; margin: auto; border-collapse: collapse; }
    #         th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    #         th { background-color: #f4f4f4; }
    #     </style>
    # </head>
    # <body>
    #     <h2 style="text-align: center;">Books List</h2>
    #     <table>
    #         <tr><th>Title</th><th>Author</th><th>Publish Date</th><th>ISBN</th></tr>
    # """
    #
    # for book in books:
    #     book_details += f"<tr><td>{book.title}</td><td>{book.author}</td><td>{book.published_date}</td><td>{book.isbn}</td></tr>"
    #
    # book_details += "</table></body></html>"

    return JsonResponse({
        'data': serializer.data
    })
