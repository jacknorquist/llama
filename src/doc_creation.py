from pathlib import Path

sample_docs = {
    "midwest_fishing_basics.txt": """
    Q: What are the most popular freshwater fish to catch in the Midwest?
    A: Common species include largemouth bass, smallmouth bass, walleye, northern pike, muskellunge (muskie), crappie, bluegill, catfish, and perch.

    Q: What fishing methods are commonly used in the Midwest?
    A: Anglers often use spin fishing, baitcasting, fly fishing, and ice fishing depending on the season and target species.

    Q: When is the best time of year to fish in the Midwest?
    A: Spring and fall are ideal for bass and walleye. Ice fishing is popular in winter, especially from December through February.

    Q: Do I need a fishing license to fish in the Midwest?
    A: Yes. Each state in the Midwest—such as Wisconsin, Minnesota, Illinois, Indiana, and Michigan—requires anglers to purchase a fishing license. Regulations vary by state and species.

    Q: Are there limits on how many fish I can keep?
    A: Yes. Bag limits and size restrictions vary by state and species. For example, in Wisconsin, the daily bag limit for walleye is typically 3–5 fish depending on the lake.

    Q: Where can I check local fishing regulations?
    A: Visit each state’s Department of Natural Resources (DNR) website or pick up a printed regulation booklet from local bait shops.

    Q: What baits work best for bass in Midwest lakes?
    A: Plastic worms, crankbaits, spinnerbaits, and topwater lures are all effective for largemouth and smallmouth bass.

    Q: How do I find good fishing spots in the Midwest?
    A: Look for drop-offs, weed lines, submerged structures, and points. Local lakes like Lake Erie (for walleye) and Lake Minnetonka (for bass) are hotspots.

    Q: Can I fish year-round in the Midwest?
    A: Yes. Open water fishing is possible spring through fall, and ice fishing is very popular in northern states during winter.

    Q: When is the best time to fish for walleye in clear water lakes?
    A: In clear water, walleyes are more likely to feed during low-light periods such as early morning, dusk, or overcast days. This is because they are light-sensitive and prefer dim conditions for ambushing prey.

    Q: Where can I find the best walleye fishing in the Midwest?
    A: Many rivers across the Midwest offer excellent walleye fishing opportunities. Additionally, the Great Lakes—particularly Lake Erie and Lake Michigan—support strong walleye populations and provide both inland and big-water fishing experiences.

    Q: What types of bait work best for catching walleye?
    A: Live bait such as minnows, leeches, and nightcrawlers are highly effective for catching walleye. Jigs tipped with bait are especially popular in both rivers and lakes.

    Q: What other species can I target in the Great Lakes besides traditional Midwest fish?
    A: The Great Lakes provide additional species not common in smaller inland waters, including Chinook and Coho salmon, lake trout, and steelhead.

    Q: What are steelhead and where can I catch them?
    A: Steelhead are a migratory form of rainbow trout that live most of their lives in large bodies of water like the Great Lakes, but spawn in freshwater tributaries. They can be caught in rivers that flow into the Great Lakes, especially in spring and fall.

    Q: Where are natural trout streams located in the Midwest?
    A: Many natural trout streams can be found in the Driftless Area, which includes southeastern Minnesota, southwestern Wisconsin, northeastern Iowa, and northwestern Illinois. This region was untouched by glaciers during the last ice age, resulting in spring-fed creeks ideal for trout habitat.

    Q: What types of trout are found in the Driftless Area?
    A: Stream trout species in the Driftless Area include brook trout (native), brown trout (introduced), and rainbow trout. These streams often support catch-and-release or fly fishing opportunities.

    Q: What should I know about ice fishing in the Midwest?
    A: Ice fishing is popular in states like Minnesota, Wisconsin, and Michigan. Always check ice thickness—4 inches minimum for walking, 8–12 inches for vehicles. Use tip-ups, jigging rods, and live bait like minnows or waxworms for panfish, walleye, and northern pike.

    Q: What gear is recommended for beginners fishing in Midwest lakes?
    A: A medium spinning combo (6'6" rod, 2500 reel), 8–10 lb monofilament line, and a basic tackle box with hooks, sinkers, plastic worms, and crankbaits is ideal for starters targeting bass and panfish.

    Q: Should I fish from shore or a boat in the Midwest?
    A: Both are effective. Boats allow access to deeper or offshore structure, while shore fishing is great near docks, bridges, and public piers—especially in spring and fall when fish are shallow.

    Q: Are there rules for transporting fish I’ve caught?
    A: Yes. Most Midwest states require fish to be transported with skin on for identification. Some areas require guts removed for filleting. Always check your state DNR’s transport and possession regulations.

    Q: Is night fishing legal and productive in the Midwest?
    A: Yes. Night fishing is legal in most states and can be very productive, especially for catfish, walleye, and bass during summer. Use glow-in-the-dark bobbers or lighted lures. Always bring safety lights and check local curfews or boating rules.

    Q: When is the best time to fish for crappies in the Midwest?
    A: Spring is the prime season for crappie fishing, especially during the spawning period when they move into shallow water. Look for them near brush piles, submerged wood, or shoreline vegetation in 2 to 6 feet of water. Light jigs or minnows under a bobber work well.
    """
}


raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

for filename, content in sample_docs.items():
    (raw_dir / filename).write_text(content.strip(), encoding="utf-8")

