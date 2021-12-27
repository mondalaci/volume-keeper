module.exports = {
  apps : [{
    name: 'volume-keeper',
    script: 'volume-keeper.py',
    watch: true,
    ignore_watch: ['logs'],
    error_file: 'logs/err.log',
    out_file: 'logs/out.log',
    merge_logs: true,
  }],
};
