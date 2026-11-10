# Poznámky k podobným pracím

Pracovní podklad pro páteř v [backbone.md](backbone.md). Není to provozní manuál a nemění přijaté ADR.

Nejbližší koncepce, kterou lze v projektech použít hned: **oficiální workflow Spec Kitu `speckit`**. Člověk dodá jednu krátkou kartu otočky. Model v pevných krocích udělá specifikaci, plán, úkoly a implementaci. Člověk schválí specifikaci a plán, než se pokračuje. Stav běhu zůstává v `.specify/workflows/runs/`.

To je Anthropicovo řetězení promptů s lidskou bránou, nasazené na nástroj, který už máte. DEV|L zůstává významem karty (jedna nejistota, důkaz, odklad). Není to druhý systém vedle Spec Kitu.

## Co vzít

### Spec Kit — Full SDD Cycle

Zdroj: [Workflows](https://github.github.com/spec-kit/reference/workflows.html), vestavěné `workflow.yml` s id `speckit`.

Řetěz je `speckit.specify` → brána → `speckit.plan` → brána → `speckit.tasks` → `speckit.implement`. Vstup je jeden text `spec`. Brána při odmítnutí běh ukončí. Schválení pokračuje. Běh lze přerušit a navázat přes `specify workflow resume`.

Použití: toto je automatizace vývoje. Okolní příkazy (`clarify`, `checklist`, `analyze`, `converge`) se volají ručně, jen když brána ukáže mezeru. Do páteře nepatří.

Ověřené omezení: krok typu `prompt` posílá text agentovi a spolehlivě vrací kód ukončení. Zachycení celé odpovědi pro další krok bylo v implementaci označeno jako plánované, ne hotové. Páteř proto nesmí stavět na tom, že model napíše brief a workflow ho samo vloží do `specify`. Brief píše člověk. Model ho rozpracuje až uvnitř `speckit.specify`, který ukládá `spec.md`.

Preset s `strategy: append` je správné místo pro pár polí, která šablona Spec Kitu nemá. Obalení příkazu `speckit.specify` vlastním zněním by s ním soutěžilo. Overlay umí vložit krok, neumí přidat vstup. Na páteř overlay potřeba není.

### Anthropic — workflow, ne autonomní agent

Zdroj: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

Řetěz s předem danými kroky a kontrolou mezi nimi je pro známou práci spolehlivější než model, který si řídí postup. Routing na jeden specializovaný prompt dává smysl, až když se vstupy opravdu liší. Čtyři role v jednom kroku jsou orchestrace, kterou páteř nepotřebuje.

Použití: jeden běh, jeden vstup, brány na artefaktech Spec Kitu. Rolový prompt až jako pozdější rozšíření, když jedna karta přestane stačit.

### Hevner — tři cykly design science

Zdroj: Hevner, *A Three Cycle View of Design Science Research* (2007). Relevance bere problém z prostředí a vrací artefakt do provozu. Rigor bere znalost a vrací novou. Design uprostřed staví a hodnotí.

Použití: jedna otočka řeší jednu nejistotu a končí pozorováním v provozu, ne sloučením testů. Pojmenování Engineer / Scientist / Business je až pozdější čočka. V páteři stačí řádek na kartě, čeho se otočka týká.

### Dual-track a living lab

Discovery rozhoduje, co stojí za stavbu. Delivery to staví. Living lab a action design research k tomu přidávají zásah v reálném prostředí a učení z něj. Skill `field-chain` už říká totéž pro první řetězec dat až na výstup v místě.

Použití: karta nese „kde se to ověří v provozu“. Po implementaci workflow končí. Další otočka začíná novou kartou s tím, co se skutečně stalo. Skill se čte jen když otočka zavádí nebo mění provozní řetězec.

### BMAD

Zdroj: srovnání BMAD a Spec Kitu (2025–2026). BMAD dává týmu persony a vlastní strom artefaktů (PRD, architektura, story). Vedle Spec Kitu vzniknou dvě autority pro tutéž práci a obřad i pro malou změnu.

Použití: žádné. Je to tvar, kterému se ai-promptkit už jednou vyhnul v ADR-0001 a ADR-0002.

### Stupnice připravenosti (TRL a příbuzné)

NASA TRL, KTH Innovation Readiness Level, Integrated Readiness Matrix a Breakdown T&BRL jsou diagnostika pro financování a přenos. Lineární stupnice tlačí k nasazení. TAČR stupnici TRL mluví, takže hlášení projektu ji bude potřebovat.

Použití: později, jako odstavec v návrhu projektu. Mapuje se z důkazu v `specs/`, není motorem otoček.

## Co do páteře nepatří

- Spouštění Engineer, Scientist, Business a Projectant jako podmínka každé otočky.
- Návrh projektu, článek a balík pro praxi jako kroky workflow.
- Druhý deník zralosti vedle `.specify/` a `specs/`.
- Devět stupňů TRL jako přechody mezi feature.
- Vlastní workflow, které kopíruje `speckit` a přidává krok závislý na nezachyceném výstupu promptu.

## Návrh úprav ekosystému

Páteř se nasazuje vedle stávajícího textu. V tomto kroku se role, preset a ADR nemění. Až se páteř osvědčí, úpravy jsou tyto:

| Místo | Úprava |
|-------|--------|
| [README.md](../README.md) | První cesta je karta a `specify workflow run speckit`. Kaskáda nápad → návrh → článek / praxe se označí jako rozšíření. |
| [docs/manual.md](manual.md) | Odkaz na [backbone.md](backbone.md) jako provoz jedné otočky. Dnešní postup se čtyřmi agenty zůstane v části „rozšíření“. |
| [spec-kit/presets/devl-spiral/templates/spec-addendum.md](../spec-kit/presets/devl-spiral/templates/spec-addendum.md) | Nechat jen nejistotu, zděděný důkaz, cíl ověření v provozu a odklady. Problém a rozsah patří nativní šabloně specifikace. |
| [spec-kit/presets/devl-spiral/templates/plan-addendum.md](../spec-kit/presets/devl-spiral/templates/plan-addendum.md) | Nechat společné povinnosti (jednotky, provenance, provozní důkaz). Grade sekce sloučit do jedné, dokud role nejsou v páteři. |
| [spec-kit/presets/devl-spiral/templates/constitution-addendum.md](../spec-kit/presets/devl-spiral/templates/constitution-addendum.md) | Čtyři věty: jedna nejistota na otočku, brána člověka, důkaz označený jako fakt nebo předpoklad, žádný druhý deník vývoje. |
| `agents/` | Přestanou být způsob, jak otočku začít. Zůstanou volitelné čtení, až karta nestačí. |
| `skills/` | Beze změny obsahu. Čtou se na vyžádání, workflow je nenačítá. |
| `prompts/doctor.md`, `upgrade.md`, `takeover.md` | Beze změny role. Doctor později zkontroluje, že aktivní `spec.md` má jednu nejistotu. |

ADR-0002 a ADR-0004 se nemažou. Až páteř nahradí dnešní start otočky, doplní se krátké ADR: delivery je vestavěné workflow `speckit`, Develop je karta na jeho vstupu.
