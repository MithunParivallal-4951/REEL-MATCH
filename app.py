<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Film Archive — Movie Database</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:    #f3eee3;
    --paper-2:  #ece4d4;
    --card:     #fbf8f1;
    --ink:      #2a2520;
    --ink-dim:  #6f6457;
    --ink-faint:#a89c8c;
    --rule:     #d8cdb9;
    --rule-dark:#c2b49a;
    --accent:   #b5402c;
    --accent-2: #2f5a4f;
    --gold:     #c08a35;

    --radius: 3px;
    --container: 1180px;
  }

  *{ box-sizing: border-box; }

  body{
    margin:0;
    background: var(--paper);
    color: var(--ink);
    font-family: 'Inter', system-ui, sans-serif;
    line-height: 1.5;
    background-image:
      repeating-linear-gradient(180deg, transparent, transparent 31px, rgba(0,0,0,0.025) 32px);
  }

  a{ color: var(--accent); text-decoration: none; }
  a:hover{ text-decoration: underline; }

  ::selection{ background: var(--gold); color: var(--card); }

  :focus-visible{
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }

  /* ============ Header / Ledger title ============ */
  header{
    border-bottom: 3px double var(--rule-dark);
    padding: clamp(28px, 5vw, 48px) clamp(16px, 4vw, 40px) clamp(20px, 4vw, 32px);
  }
  .header-inner{
    max-width: var(--container);
    margin: 0 auto;
    display:flex;
    justify-content: space-between;
    align-items: flex-end;
    gap: 24px;
    flex-wrap: wrap;
  }
  .header-right{
    display:flex;
    flex-direction:column;
    align-items:flex-end;
    gap: 12px;
  }
  .btn-back{
    display:inline-flex;
    align-items:center;
    gap: 7px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: .76rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: var(--ink-dim);
    border: 1px solid var(--rule-dark);
    border-radius: 3px;
    padding: 8px 14px;
    text-decoration: none;
    transition: border-color .15s ease, color .15s ease;
    white-space: nowrap;
  }
  .btn-back:hover{
    border-color: var(--accent);
    color: var(--accent);
    text-decoration: none;
  }
  .archive-mark{
    font-family: 'IBM Plex Mono', monospace;
    font-size: .7rem;
    letter-spacing: .25em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 10px;
  }
  h1{
    font-family: 'Fraunces', serif;
    font-weight: 600;
    font-size: clamp(2.4rem, 6vw, 4rem);
    margin: 0;
    letter-spacing: -.01em;
    line-height: 1;
  }
  .header-meta{
    font-family: 'IBM Plex Mono', monospace;
    font-size: .82rem;
    color: var(--ink-dim);
    text-align: right;
    line-height: 1.7;
  }
  .header-meta strong{ color: var(--ink); font-weight: 600; }

  /* ============ Layout ============ */
  main{
    max-width: var(--container);
    margin: 0 auto;
    padding: clamp(20px, 4vw, 36px) clamp(16px, 4vw, 40px) 80px;
  }

  /* ============ Control bar (search / filter / sort) ============ */
  .control-bar{
    display:flex;
    gap: 14px;
    flex-wrap: wrap;
    align-items: flex-end;
    padding-bottom: 22px;
    border-bottom: 1px solid var(--rule);
    margin-bottom: 26px;
  }
  .field{
    display:flex;
    flex-direction:column;
    gap: 6px;
  }
  .field label{
    font-family: 'IBM Plex Mono', monospace;
    font-size: .68rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: var(--ink-dim);
  }
  .field input[type="text"],
  .field select{
    background: var(--card);
    border: 1px solid var(--rule-dark);
    border-radius: var(--radius);
    padding: 10px 12px;
    font-family: 'Inter', sans-serif;
    font-size: .95rem;
    color: var(--ink);
    min-height: 42px;
  }
  .field input[type="text"]:focus,
  .field select:focus{
    border-color: var(--accent);
  }
  .field.search{ flex: 2 1 260px; }
  .field.genre{ flex: 1 1 160px; }
  .field.sort{ flex: 1 1 160px; }

  .btn{
    background: var(--ink);
    color: var(--paper);
    border: none;
    border-radius: var(--radius);
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: .1em;
    text-transform: uppercase;
    font-size: .78rem;
    padding: 0 22px;
    min-height: 42px;
    cursor: pointer;
    transition: background .15s ease;
  }
  .btn:hover{ background: var(--accent); }

  .btn-ghost{
    background: transparent;
    color: var(--ink-dim);
    border: 1px solid var(--rule-dark);
    border-radius: var(--radius);
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: .1em;
    text-transform: uppercase;
    font-size: .72rem;
    padding: 0 16px;
    min-height: 42px;
    cursor: pointer;
    text-decoration: none;
    display:inline-flex;
    align-items:center;
  }
  .btn-ghost:hover{
    border-color: var(--accent);
    color: var(--accent);
    text-decoration:none;
  }

  /* ============ Result summary ============ */
  .result-summary{
    font-family: 'IBM Plex Mono', monospace;
    font-size: .8rem;
    color: var(--ink-dim);
    margin-bottom: 18px;
    display:flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
  }
  .result-summary .active-filter{
    color: var(--accent);
  }
  .result-summary .clear{
    color: var(--ink-dim);
    text-decoration: underline;
  }

  /* ============ Card grid ============ */
  .grid{
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    gap: 18px;
  }
  .card{
    background: var(--card);
    border: 1px solid var(--rule);
    border-radius: var(--radius);
    padding: 16px 18px;
    display:flex;
    flex-direction:column;
    gap: 10px;
    position: relative;
    transition: border-color .15s ease, transform .15s ease, box-shadow .15s ease;
  }
  .card:hover{
    border-color: var(--accent);
    transform: translateY(-2px);
    box-shadow: 0 6px 18px -10px rgba(42,37,32,.35);
  }
  .card-id{
    position:absolute;
    top: 12px;
    right: 14px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: .68rem;
    color: var(--ink-faint);
  }
  .card-title{
    font-family: 'Fraunces', serif;
    font-weight: 600;
    font-size: 1.18rem;
    line-height: 1.25;
    padding-right: 36px;
  }
  .card-title a{
    color: var(--ink);
  }
  .card-title a:hover{
    color: var(--accent);
    text-decoration: none;
  }
  .card-meta{
    font-family: 'IBM Plex Mono', monospace;
    font-size: .76rem;
    color: var(--ink-dim);
    display:flex;
    flex-wrap: wrap;
    gap: 6px 14px;
  }
  .card-rating{
    color: var(--gold);
    font-weight: 600;
  }
  .card-genres{
    font-size: .72rem;
    color: var(--accent-2);
    text-transform: uppercase;
    letter-spacing: .08em;
  }
  .card-desc{
    font-size: .87rem;
    color: var(--ink-dim);
    line-height: 1.55;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .card-director{
    font-size: .8rem;
    color: var(--ink-faint);
    margin-top: auto;
    border-top: 1px solid var(--rule);
    padding-top: 8px;
  }

  .empty-state{
    text-align:center;
    padding: 60px 20px;
    color: var(--ink-dim);
    font-family: 'IBM Plex Mono', monospace;
    border: 1px dashed var(--rule-dark);
    border-radius: var(--radius);
  }

  /* ============ Pagination ============ */
  .pagination{
    display:flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    margin-top: 40px;
    flex-wrap: wrap;
    font-family: 'IBM Plex Mono', monospace;
    font-size: .8rem;
  }
  .pagination a, .pagination span{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    min-width: 38px;
    height: 38px;
    border: 1px solid var(--rule-dark);
    border-radius: var(--radius);
    color: var(--ink);
    text-decoration: none;
    padding: 0 8px;
  }
  .pagination a:hover{
    border-color: var(--accent);
    color: var(--accent);
    text-decoration: none;
  }
  .pagination .current{
    background: var(--ink);
    color: var(--paper);
    border-color: var(--ink);
  }
  .pagination .disabled{
    color: var(--ink-faint);
    border-color: var(--rule);
    cursor: default;
  }
  .pagination .ellipsis{
    border: none;
    color: var(--ink-faint);
  }

  footer{
    border-top: 3px double var(--rule-dark);
    text-align:center;
    color: var(--ink-dim);
    font-family: 'IBM Plex Mono', monospace;
    font-size: .76rem;
    letter-spacing: .08em;
    padding: 24px 20px;
  }

  @media (max-width: 640px){
    .control-bar{ flex-direction: column; align-items: stretch; }
    .field.search, .field.genre, .field.sort{ flex: 1 1 auto; }
    .header-meta{ text-align: left; }
  }
</style>
</head>
<body>

<header>
  <div class="header-inner">
    <div>
      <div class="archive-mark">Catalog No. 16-K · Motion Picture Index</div>
      <h1>Film Archive</h1>
    </div>
    <div class="header-right">
      <div class="header-meta">
        <strong>{{ total }}</strong> entries on record<br>
        Page <strong>{{ page }}</strong> of <strong>{{ total_pages }}</strong>
      </div>
      <a href="http://127.0.0.1:5000" target="_blank" class="btn-back">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
        Reel Match
      </a>
    </div>
  </div>
</header>

<main>
  <form class="control-bar" method="get" action="/">
    <div class="field search">
      <label for="q">Search by title</label>
      <input type="text" id="q" name="q" value="{{ search }}" placeholder="e.g. Dark Knight, Spirited Away…" autocomplete="off">
    </div>
    <div class="field genre">
      <label for="genre">Genre</label>
      <select id="genre" name="genre">
        <option value="">All genres</option>
        {% for g in genres %}
        <option value="{{ g }}" {% if g == genre %}selected{% endif %}>{{ g }}</option>
        {% endfor %}
      </select>
    </div>
    <div class="field sort">
      <label for="sort">Sort by</label>
      <select id="sort" name="sort">
        <option value="title" {% if sort == 'title' %}selected{% endif %}>Title (A–Z)</option>
        <option value="rating_desc" {% if sort == 'rating_desc' %}selected{% endif %}>Rating (high–low)</option>
        <option value="rating_asc" {% if sort == 'rating_asc' %}selected{% endif %}>Rating (low–high)</option>
        <option value="votes_desc" {% if sort == 'votes_desc' %}selected{% endif %}>Most voted</option>
        <option value="newest" {% if sort == 'newest' %}selected{% endif %}>Release date (newest)</option>
        <option value="oldest" {% if sort == 'oldest' %}selected{% endif %}>Release date (oldest)</option>
      </select>
    </div>
    <button type="submit" class="btn">Search</button>
    {% if search or genre or sort != 'title' %}
    <a href="/" class="btn-ghost">Reset</a>
    {% endif %}
  </form>

  <div class="result-summary">
    <div>
      Showing {{ movies|length }} of <strong>{{ total }}</strong> records
      {% if search %}for title containing <span class="active-filter">&ldquo;{{ search }}&rdquo;</span>{% endif %}
      {% if genre %}in genre <span class="active-filter">{{ genre }}</span>{% endif %}
    </div>
  </div>

  {% if movies %}
  <div class="grid">
    {% for m in movies %}
    <article class="card">
      <span class="card-id">#{{ m.id }}</span>
      <h2 class="card-title"><a href="/movie/{{ m.id }}">{{ m.title }}</a></h2>
      <div class="card-meta">
        <span>{{ m.release_date }}</span>
        {% if m.duration %}<span>{{ m.duration }}</span>{% endif %}
        {% if m.rating %}<span class="card-rating">★ {{ "%.1f"|format(m.rating) }}</span>{% endif %}
        {% if m.votes %}<span>{{ "{:,}".format(m.votes|int) }} votes</span>{% endif %}
      </div>
      {% if m.genres %}
      <div class="card-genres">{{ m.genres.replace(',', ' · ') }}</div>
      {% endif %}
      {% if m.directed_by %}
      <div class="card-director">Directed by {{ m.directed_by }}</div>
      {% endif %}
    </article>
    {% endfor %}
  </div>

  <nav class="pagination" aria-label="Pagination">
    {% set qs = '&q=' + search|urlencode + '&genre=' + genre|urlencode + '&sort=' + sort %}
    {% if page > 1 %}
      <a href="/?page=1{{ qs }}">&laquo;</a>
      <a href="/?page={{ page - 1 }}{{ qs }}">&lsaquo; Prev</a>
    {% else %}
      <span class="disabled">&laquo;</span>
      <span class="disabled">&lsaquo; Prev</span>
    {% endif %}

    {% set window = 2 %}
    {% for p in range(1, total_pages + 1) %}
      {% if p == 1 or p == total_pages or (p >= page - window and p <= page + window) %}
        {% if p == page %}
          <span class="current">{{ p }}</span>
        {% else %}
          <a href="/?page={{ p }}{{ qs }}">{{ p }}</a>
        {% endif %}
      {% elif p == page - window - 1 or p == page + window + 1 %}
        <span class="ellipsis">&hellip;</span>
      {% endif %}
    {% endfor %}

    {% if page < total_pages %}
      <a href="/?page={{ page + 1 }}{{ qs }}">Next &rsaquo;</a>
      <a href="/?page={{ total_pages }}{{ qs }}">&raquo;</a>
    {% else %}
      <span class="disabled">Next &rsaquo;</span>
      <span class="disabled">&raquo;</span>
    {% endif %}
  </nav>
  {% else %}
  <div class="empty-state">
    No records match this search.<br>
    <a href="/">Clear filters and return to the full index.</a>
  </div>
  {% endif %}
</main>

<footer>Film Archive Database &middot; SQLite-backed catalog of {{ total }} titles</footer>

</body>
</html>
