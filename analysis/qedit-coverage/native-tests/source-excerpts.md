# Source evidence

## main.pas lines 5589-5620

SHA-256: `10a103f9d99059c0875f0acf953cc1e3015889caf5196a072b87dfe9eb001e1d`

```text

    // rebuild the virtual file
    di := allocmem(5000000);

    F1 := 0;
    // bin file
    if not isdc then
    begin
      if SaveDialog1.FilterIndex = 5 then
      begin
        d := 4652;
        move(d, di[F1], 4);
        inc(F1, 4);
        d := y + 4652;
        move(d, di[F1], 4);
        inc(F1, 4);
        d := (x * 4) + y + 4652;
        F2 := d;
        move(d, di[F1], 4);
        inc(F1, 4);
        d := $FFFFFFFF;
        move(d, di[F1], 4);
        inc(F1, 4);
        // language and quest number
        d := qnum;
        move(d, di[F1], 4);
        inc(F1, 4);
        d := $0;
        move(d, di[F1], 4);
        inc(F1, 4);
        move(BBData[0], di[$39C], $E90);
      end
```

## Client.cc lines 412-425

SHA-256: `4716e6c7c394da13db2ab57986e64cf729075d49260846236c0583e5de709441`

```text
    std::shared_ptr<const Lobby> game,
    uint8_t event,
    Difficulty difficulty,
    size_t num_players,
    bool v1_present) const {
  if (!q->has_version_any_language(this->version())) {
    return false;
  }
  if ((q->meta.max_players > 0) && (num_players > q->meta.max_players)) {
    return false;
  }
  return this->evaluate_quest_availability_expression(
      q->meta.enabled_expression, game, event, difficulty, num_players, v1_present);
}
```
