from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Python Web Service")
HEALTH_STATUS = "healthy"

PAGE_STYLES = """
<style>
  :root {
    color-scheme: light;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #172b4d;
    background: #f5f7fb;
    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-optical-sizing: auto;
  }
  * { box-sizing: border-box; }
  body { min-width: 320px; min-height: 100vh; margin: 0; }
  a { color: inherit; }
  .shell { width: min(100% - 2.5rem, 1080px); margin-inline: auto; }
  .topbar {
    display: flex;
    min-height: 76px;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    border-bottom: 1px solid #e8edf5;
  }
  .brand { display: inline-flex; align-items: center; gap: .75rem; text-decoration: none; }
  .brand-mark {
    display: grid;
    width: 38px;
    height: 38px;
    place-items: center;
    border-radius: 12px;
    background: linear-gradient(145deg, #3768e8, #704be8);
    box-shadow: 0 5px 12px rgb(75 91 210 / 22%);
    color: #fff;
    font-size: 1.1rem;
    font-weight: 800;
  }
  .brand-name { font-size: .96rem; font-weight: 750; letter-spacing: -.02em; }
  .nav-link {
    color: #5b6b85;
    font-size: .9rem;
    font-weight: 650;
    text-decoration: none;
    transition: color .18s ease;
  }
  .nav-link:hover { color: #315de5; }
  .nav-link:focus-visible, .button:focus-visible {
    outline: 3px solid #a9bcff;
    outline-offset: 4px;
  }
  .main { padding-block: clamp(2.5rem, 7vw, 5.5rem); }
  .hero {
    position: relative;
    overflow: hidden;
    padding: clamp(2rem, 7vw, 5rem);
    border: 1px solid #e2e8f4;
    border-radius: 28px;
    background:
      radial-gradient(ellipse at 91% 10%, rgb(181 194 255 / 48%), transparent 30%),
      radial-gradient(ellipse at 6% 100%, rgb(209 226 255 / 58%), transparent 35%),
      linear-gradient(135deg, #fff 20%, #f7f8ff 100%);
    box-shadow: 0 24px 70px rgb(33 51 92 / 9%), 0 2px 6px rgb(33 51 92 / 4%);
  }
  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: .55rem;
    color: #5366bb;
    font-size: .77rem;
    font-weight: 800;
    letter-spacing: .12em;
    text-transform: uppercase;
  }
  .eyebrow-mark { width: 8px; height: 8px; border-radius: 50%; background: #6a5be8; }
  h1 {
    max-width: 720px;
    margin: 1.25rem 0 1rem;
    color: #142544;
    font-size: clamp(2.5rem, 7vw, 4.65rem);
    font-weight: 780;
    letter-spacing: -.065em;
    line-height: 1.04;
  }
  .lead {
    max-width: 590px;
    margin: 0;
    color: #61708a;
    font-size: clamp(1rem, 2vw, 1.15rem);
    line-height: 1.75;
  }
  .button {
    display: inline-flex;
    min-height: 48px;
    align-items: center;
    justify-content: center;
    gap: .6rem;
    margin-top: 2rem;
    padding: .8rem 1.15rem;
    border: 1px solid #315de5;
    border-radius: 12px;
    background: #315de5;
    box-shadow: 0 7px 16px rgb(49 93 229 / 20%);
    color: #fff;
    font-size: .93rem;
    font-weight: 700;
    text-decoration: none;
    transition: background .18s ease, box-shadow .18s ease, transform .18s ease;
  }
  .button:hover {
    transform: translateY(-1px);
    background: #244bc9;
    box-shadow: 0 10px 20px rgb(49 93 229 / 25%);
  }
  .button-arrow { font-size: 1.15rem; line-height: 1; }
  .features {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
    margin-top: 1.25rem;
  }
  .feature {
    padding: 1.25rem 1.35rem;
    border: 1px solid #e7ebf3;
    border-radius: 16px;
    background: rgb(255 255 255 / 82%);
  }
  .feature-label { color: #8490a6; font-size: .76rem; font-weight: 750; letter-spacing: .08em; text-transform: uppercase; }
  .feature-value { margin-top: .5rem; color: #263b60; font-size: .98rem; font-weight: 700; }
  .health-heading { margin-bottom: 1.5rem; }
  .health-heading h1 { margin-top: .85rem; font-size: clamp(2.2rem, 5vw, 3.4rem); }
  .health-panel {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.5rem;
    padding: clamp(1.4rem, 4vw, 2rem);
    border: 1px solid #bfe9d2;
    border-radius: 20px;
    background: linear-gradient(120deg, #f1fff7, #e8fbf1);
    box-shadow: 0 10px 28px rgb(32 120 79 / 6%);
  }
  .health-caption { color: #587568; font-size: .84rem; font-weight: 650; }
  .health-value { display: flex; align-items: center; gap: .7rem; margin-top: .45rem; color: #176b45; font-size: clamp(1.5rem, 4vw, 2rem); font-weight: 800; letter-spacing: -.035em; text-transform: capitalize; }
  .live-dot { position: relative; width: 11px; height: 11px; border-radius: 50%; background: #22a267; }
  .live-dot::after { position: absolute; inset: -5px; border: 1px solid #22a267; border-radius: 50%; content: ""; opacity: .45; }
  .health-code { padding: .65rem .8rem; border: 1px solid #d5efdf; border-radius: 10px; background: rgb(255 255 255 / 70%); color: #4a7560; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: .8rem; white-space: nowrap; }
  .section-heading { margin: 2.5rem 0 1rem; color: #253957; font-size: 1.05rem; font-weight: 750; letter-spacing: -.02em; }
  .categories { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }
  .category {
    position: relative;
    min-height: 184px;
    padding: 1.35rem;
    overflow: hidden;
    border: 1px solid var(--border);
    border-radius: 17px;
    background: var(--surface);
    transition: transform .18s ease, box-shadow .18s ease;
  }
  .category:hover { transform: translateY(-3px); box-shadow: 0 12px 24px rgb(33 51 92 / 8%); }
  .category.healthy { --accent: #198754; --border: #d3eddf; --surface: #f7fdf9; }
  .category.degraded { --accent: #b7791f; --border: #f1e4c4; --surface: #fffdf7; }
  .category.unhealthy { --accent: #c44747; --border: #f1dada; --surface: #fffafa; }
  .category-top { display: flex; align-items: center; justify-content: space-between; gap: .5rem; }
  .category-name { display: inline-flex; align-items: center; gap: .6rem; color: #263b60; font-size: 1rem; font-weight: 750; text-transform: capitalize; }
  .category-icon { display: grid; width: 30px; height: 30px; place-items: center; border-radius: 10px; background: color-mix(in srgb, var(--accent) 11%, white); color: var(--accent); font-size: .9rem; font-weight: 900; }
  .category-state { color: #8490a6; font-size: .68rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
  .category p { margin: 1.1rem 0 0; color: #6c7a91; font-size: .9rem; line-height: 1.65; }
  .category.is-current { border-color: color-mix(in srgb, var(--accent) 38%, white); box-shadow: inset 0 3px var(--accent); }
  .category.is-current .category-state { color: var(--accent); }
  .health-footer { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin-top: 1.5rem; }
  .back-link { color: #526484; font-size: .9rem; font-weight: 700; text-decoration: none; }
  .back-link:hover { color: #315de5; }
  .api-link { color: #63728b; font-size: .82rem; text-decoration: none; }
  .api-link:hover { color: #315de5; text-decoration: underline; }
  .footer { padding: 1.5rem 0 2rem; color: #8a96aa; font-size: .8rem; text-align: center; }
  @media (max-width: 700px) {
    .features, .categories { grid-template-columns: 1fr; }
    .feature { padding: 1rem 1.1rem; }
    .category { min-height: 0; }
    .health-panel { align-items: flex-start; flex-direction: column; gap: 1rem; }
    .health-code { white-space: normal; }
  }
  @media (max-width: 430px) {
    .shell { width: min(100% - 1.5rem, 1080px); }
    .topbar { min-height: 66px; }
    .brand-name { font-size: .88rem; }
    .nav-link { font-size: .82rem; }
    .hero { border-radius: 21px; }
    .health-footer { align-items: flex-start; flex-direction: column; }
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { scroll-behavior: auto !important; transition-duration: .01ms !important; }
  }
</style>
"""


def render_page(title: str, content: str) -> HTMLResponse:
    return HTMLResponse(
        f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#f5f7fb">
    <title>{title} · Python Web Service</title>
    {PAGE_STYLES}
  </head>
  <body>
    <div class="shell">
      <header class="topbar">
        <a class="brand" href="/" aria-label="Python Web Service home">
          <span class="brand-mark" aria-hidden="true">P</span>
          <span class="brand-name">Python Web Service</span>
        </a>
        <a class="nav-link" href="/health">System health <span aria-hidden="true">↗</span></a>
      </header>
      <main class="main">{content}</main>
      <footer class="footer">A lightweight service, built with FastAPI.</footer>
    </div>
  </body>
</html>"""
    )


@app.get("/")
def root() -> HTMLResponse:
    return render_page(
        "Welcome",
        """
        <section class="hero" aria-labelledby="welcome-title">
          <span class="eyebrow"><span class="eyebrow-mark"></span>Simple · Fast · Reliable</span>
          <h1 id="welcome-title">Your service is ready to go.</h1>
          <p class="lead">
            Welcome to your Python web service. Everything is up and running,
            and your health dashboard is just one click away.
          </p>
          <a class="button" href="/health">
            Explore service health <span class="button-arrow" aria-hidden="true">→</span>
          </a>
        </section>
        <section class="features" aria-label="Service overview">
          <article class="feature">
            <div class="feature-label">Framework</div>
            <div class="feature-value">FastAPI</div>
          </article>
          <article class="feature">
            <div class="feature-label">Service status</div>
            <div class="feature-value">Operational</div>
          </article>
          <article class="feature">
            <div class="feature-label">Health endpoint</div>
            <div class="feature-value">/health</div>
          </article>
        </section>
        """,
    )


@app.get("/health")
def health_page() -> HTMLResponse:
    categories = (
        (
            "healthy",
            "✓",
            "The service is operating normally and responding to requests.",
        ),
        (
            "degraded",
            "!",
            "The service is available, but one or more capabilities are impaired.",
        ),
        (
            "unhealthy",
            "×",
            "The service is unavailable or unable to handle requests.",
        ),
    )
    cards = "".join(
        f"""
        <article class="category {name}{' is-current' if name == HEALTH_STATUS else ''}"
                 {"aria-current='true'" if name == HEALTH_STATUS else ""}>
          <div class="category-top">
            <h3 class="category-name"><span class="category-icon" aria-hidden="true">{icon}</span>{name}</h3>
            <span class="category-state">{"Current" if name == HEALTH_STATUS else "Status"}</span>
          </div>
          <p>{description}</p>
        </article>"""
        for name, icon, description in categories
    )
    content = f"""
    <section class="health-heading" aria-labelledby="health-title">
      <span class="eyebrow"><span class="eyebrow-mark"></span>Service overview</span>
      <h1 id="health-title">Health dashboard</h1>
      <p class="lead">A quick look at the current status and what each health level means.</p>
    </section>
    <section class="health-panel" aria-label="Current service health">
      <div>
        <div class="health-caption">CURRENT SERVICE STATUS</div>
        <div class="health-value"><span class="live-dot" aria-hidden="true"></span>{HEALTH_STATUS}</div>
      </div>
      <code class="health-code">GET&nbsp; /api/health&nbsp; →&nbsp; {{"status": "{HEALTH_STATUS}"}}</code>
    </section>
    <h2 class="section-heading">Health categories</h2>
    <section class="categories" aria-label="Health status categories">{cards}
    </section>
    <nav class="health-footer" aria-label="Health dashboard links">
      <a class="back-link" href="/">← Back to home</a>
      <a class="api-link" href="/api/health">View JSON response</a>
    </nav>
    """
    return render_page("Service health", content)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": HEALTH_STATUS}
