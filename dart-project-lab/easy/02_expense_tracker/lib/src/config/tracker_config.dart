class TrackerConfig {
  final String currencySymbol;
  final String defaultStoragePath;

  const TrackerConfig({
    this.currencySymbol = 'Rp ',
    this.defaultStoragePath = 'data/expenses.json',
  });
}
