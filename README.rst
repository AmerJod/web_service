
- Author:   Amer Joudiah
- Date:     3/11/2019


``Web Service``: A simple web service to fetches data form the our spiders database.
====================================================================================


The solution designed of this web service is simple and wanted to show adherence to the requirements rather than overthinking it.

The existing version of the web service it is an MVP version and it has been implemented using Flask, RestAPI, Postgres, SQLAlchemy, and Redis.

For this exercise, the web spiders project and web service project have been merged into one solution project- for demo purpose (docker-compose). I have structured the projects in a way where we can maintain and reduce the complexity of the code, in addition, to reduce code redundancy.

I have implemented 3 projects:
    - ``spiderlib``: it is a common library (https://github.com/AmerJod/common) that used between spiders and webservice project. I built it as package, and it has been added to web_spiders_ and  web_service_ as git submodule.
       it contains 2 modules
        - db
        - logging

    - ``web sepider``: it is group of web spider that scrape a website and getting information from it (https://github.com/AmerJod/web_spiders). it contains 5 spiders that run on certain time ``[all days, at 11 am and 11 pm]``:
        - Default Spider
        - Infinite Scroll Spider
        - Javascript Spider
        - Login Spider
        - Tableful Spider


    - ``web service``: it is the web api (https://github.com/AmerJod/web_spiders), I build as package that uses uWSGI web server.



API Endpoints
=============
The Flask app provides static endpoints for each entity in the spider's database. I implemented a smart caching technique using redis server. I build a python decorator and called it ``cache_it`` that takes 3 parameters for caching the endpoint.
    .. code-block:: python

        def cache_it(default_key=None, entity_name=None, timeout=60):
            """
            Caching decorator
            deals only with one key
             Args:
                default_key: key name
                entity_name: the class name
                timeout (int): timeout for cached data
             Return:
                data
            """
            def cache(func):
                @functools.wraps(func)
                def wrapper_debug(*args, **kwargs):
                    key_name = default_key

                    list_keys = [v for k, v in kwargs.items()]
                    if len(list_keys) > 0:
                        # Get only the first key
                        key_name = list_keys[0]

                    if key_name:
                        data = get_cache(key_name=key_name, entity_name=entity_name)
                        if data:
                            # Get data from caching server
                            return data

                    # Get data from db
                    data = func(*args, **kwargs)

                    if data:
                        # Cache the data before return it
                        set_cache(key_name=key_name,data=data, entity_name=entity_name,timeout=timeout)
                        # logger.debug(f"{func.__ca!r} returned {value!r}")

                    return data
                return wrapper_debug
            return cache


         # EXAMPLE
         @cache_it(default_key='all_authors', entity_name='Author', timeout=60)
         def get(self, author_name=None):
                ...



Endpoints are reachable like this:

1.  ``Authors:``
        - ``/api/{api_version}/authors``: Gets all the authors' data with all the nested data such as quotes/tags objects for each author (eager loading).
        - ``/api/{api_version}/authors/filter/<author_name>``: Gets the author's data, including its quotes/tags.

2.  ``Quotes``:
        - ``/api/{api_version}/quotes``: Gets all the quotes' data with all the nested data such as author/tags objects for each quote (eager loading).
        - ``/api/{api_version}/quotes/filter/<author_name>``: Gets quotes data for a specific author.

3.  ``Tags``:
        - ``api/{api_version}/tags``: Gets all the tags objects.


The Database model
==================

            Below you can see all the db models:

            .. code-block:: python

                class Author(Base):
                    """
                    Author table
                         - One to many with Ouote table
                    """
                        __tablename__ = "authors"
                        author_id = Column(Integer, primary_key=True)
                        author_name = Column(String(50))
                        date_of_birth = Column(String)
                        city = Column(String(50))
                        country = Column(String(50))
                        description = Column(String)
                        quotes = relationship("Quote", back_populates="author", lazy=False)


                class Quote(Base):
                    """
                    Quote table
                        - Many to many Tag table
                        - Many to one with Author table
                    """
                        __tablename__ = "quotes"
                        quote_id = Column(Integer, primary_key=True)
                        text = Column(String)
                        author_id = Column(Integer, ForeignKey("authors.author_id"))
                        author = relationship("Author", back_populates="quotes")
                        tags = relationship("Tag", secondary=association_table)


                class Tag(Base):
                    """
                    Tag table
                        - Many to many with Quote table
                    """
                        __tablename__ = "tags"
                        tag_id = Column(Integer, primary_key=True)
                        tag = Column(String(64))
                        top_ten = Column(Boolean, default=False)


                # Many to many relationship table 'quotes_tags'
                association_table = Table(
                    "quotes_tags",
                    Base.metadata,
                    Column("quote_id", Integer, ForeignKey("quotes.quote_id")),
                    Column("tag_id", Integer, ForeignKey("tags.tag_id")),
)


Improvements
============
Again it is difficult to know what the exact requirements are. However this solution could improve substantially especially when we scale up the project and the data received into it
if:

1.  Indexes are created to speed up reads from database.
2.  I tried as much as I can to abstract each project, and remove all the dependency between them. However, for the testing purposes, we have to comprise.
    such as, as microservices architecture, each microservice has it is own data storage. In our project, web spiders and web server projects are using the same data storage.
3.  The web spiders are just inserting records into the DB, not updating existing records. This functionality needs to be added later.
4.  Implement proxying for the web spiders, to avoid being blocked.
5.  Add the ability of pause and resume the scraping job from where it's been left.
4-  Unittest is important, all of the 3 projects should have a decent amount of unnittests.


Install and Run
================
All the project are provided as containerised applications.
on the root of the prject: run

``docker-compose up --biuld``


*NB1*: Please Note, if you want to run the clone the project and run it, make sure that you get all the ``git submodules`` install into the project: ``git submodule add link``, Also create a ``python env`` and install all the packages into it,
